"""Fast Windows application discovery without the legacy monolith."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import unicodedata
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path


def _normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(r"\b(?:collegamento|shortcut|app|application|launcher)\b", " ",
                   value.casefold())
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


@dataclass(frozen=True)
class AppTarget:
    label: str
    path: Path
    score: float


class WindowsAppLauncher:
    """Resolve installed apps from known executables and Start Menu links."""

    def __init__(self, *, roots=None, startfile=None, popen=None, environ=None):
        self.environ = dict(os.environ if environ is None else environ)
        self._startfile = startfile or getattr(os, "startfile", None)
        self._popen = popen or subprocess.Popen
        self.roots = list(roots) if roots is not None else self._default_roots()
        self._index: list[tuple[str, Path]] | None = None

    def _default_roots(self) -> list[Path]:
        env = self.environ
        values = [
            Path(env.get("APPDATA", "")) / "Microsoft/Windows/Start Menu/Programs",
            Path(env.get("PROGRAMDATA", "")) / "Microsoft/Windows/Start Menu/Programs",
            Path(env.get("USERPROFILE", str(Path.home()))) / "Desktop",
            Path(env.get("PUBLIC", "")) / "Desktop",
        ]
        return [path for path in values if str(path) and path.is_dir()]

    def launch(self, name: str) -> str:
        query = _normalized(name)
        if not query:
            raise LookupError("Indica quale applicazione devo aprire.")
        explicit = Path(str(name).strip(' "')).expanduser()
        if explicit.is_file() and explicit.suffix.casefold() in {".exe", ".lnk", ".url"}:
            self._launch_path(explicit)
            return explicit.stem
        known = self._known_target(query)
        if known:
            self._launch_path(known)
            return known.stem
        target = self.find(query)
        if target is None:
            raise LookupError(f"Applicazione non trovata: {name}")
        self._launch_path(target.path)
        return target.label

    def find(self, name: str) -> AppTarget | None:
        query = _normalized(name)
        if not query:
            return None
        ranked = []
        for label, path in self._application_index():
            if "uninstall" in label or "disinstalla" in label:
                continue
            if label == query:
                score = 1.0
            elif query in label:
                score = .92 - min(.2, (len(label) - len(query)) / 100)
            elif label in query:
                score = .86
            else:
                score = SequenceMatcher(None, query, label).ratio()
            if score >= .64:
                ranked.append(AppTarget(path.stem, path, score))
        return max(ranked, key=lambda item: (item.score, -len(str(item.path)))) if ranked else None

    def _application_index(self):
        if self._index is not None:
            return self._index
        found: list[tuple[str, Path]] = []
        seen = set()
        for root in self.roots:
            try:
                candidates = root.rglob("*")
                for path in candidates:
                    if path.suffix.casefold() not in {".lnk", ".url", ".exe"}:
                        continue
                    key = str(path).casefold()
                    if key in seen:
                        continue
                    seen.add(key)
                    label = _normalized(path.stem)
                    if label:
                        found.append((label, path))
                    if len(found) >= 5000:
                        break
            except OSError:
                continue
        self._index = found
        return found

    def _known_target(self, query: str) -> Path | None:
        env = self.environ
        program_files = [env.get("PROGRAMFILES"), env.get("PROGRAMFILES(X86)"),
                         env.get("LOCALAPPDATA")]
        relatives = {
            "obs": ["obs-studio/bin/64bit/obs64.exe"],
            "obs studio": ["obs-studio/bin/64bit/obs64.exe"],
            "chrome": ["Google/Chrome/Application/chrome.exe"],
            "google chrome": ["Google/Chrome/Application/chrome.exe"],
            "spotify": ["Spotify/Spotify.exe"],
            "curseforge": ["Programs/CurseForge Windows/CurseForge.exe"],
        }
        for base in program_files:
            if not base:
                continue
            for relative in relatives.get(query, []):
                candidate = Path(base) / relative
                if candidate.is_file():
                    return candidate
        executable = shutil.which(query)
        return Path(executable) if executable else None

    def _launch_path(self, path: Path) -> None:
        path = path.resolve()
        if path.suffix.casefold() in {".lnk", ".url"}:
            if not self._startfile:
                raise RuntimeError("Apertura collegamenti disponibile solo su Windows.")
            self._startfile(str(path))
            return
        self._popen([str(path)], cwd=str(path.parent), shell=False,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
