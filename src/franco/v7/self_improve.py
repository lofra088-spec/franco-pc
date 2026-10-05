"""Autonomous self-repair for Franco V7.

Franco reads its own source, asks the model for a surgical change, applies it
on top of an in-memory snapshot, verifies that the package still compiles and
imports, and only then keeps the edit. Any failure rolls every touched file
back to its exact previous bytes.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import ClassVar

from .contracts import Brain

DENY_NAMES = {"_monolith.py", "_monolith.py.pre_orb_backup", "__init__.py"}
DENY_PARTS = {"__pycache__", ".git"}
MAX_FILE_CHARS = 60_000
MAX_TOTAL_CONTEXT = 60_000
MAX_CHANGES = 8
MAX_WRITE_CHARS = 160_000
_COMPLETE_KEYS = ("changes", "edits", "modifiche", "files", "patches")

SYSTEM_PROMPT = (
    "Sei il modulo di auto-modifica di FRANCO V7, un assistente Python. "
    "Ricevi il codice sorgente reale del pacchetto franco e una richiesta "
    "dell'utente che descrive un bug o un miglioramento di FRANCO stesso. "
    "Il tuo compito e' produrre la modifica minima e corretta che risolve "
    "davvero il problema, senza rompere nulla. Usa un patch chirurgico "
    "quando cambi poche righe; usa write solo per file nuovi o riscritture "
    "complete. Il testo 'old' deve combaciare ESATTAMENTE con il file "
    "attuale, spazi e indentazione inclusi. Rispondi SOLO con un oggetto "
    "JSON valido, nessun altro testo, in questo formato:\n"
    '{"summary": "spiegazione breve in italiano", "changes": ['
    '{"path": "v7/runtime.py", "action": "patch", "old": "testo esatto", '
    '"new": "testo sostitutivo"}, '
    '{"path": "v7/nuovo.py", "action": "write", "content": "contenuto completo"}'
    "]}\n"
    "Se non serve alcuna modifica rispondi {\"summary\": \"...\", "
    "\"changes\": []}. Non toccare mai _monolith.py ne' file .env."
)


@dataclass
class Change:
    path: str
    action: str
    content: str = ""
    old: str = ""
    new: str = ""


@dataclass
class RunResult:
    status: str
    summary: str
    applied: list[str] = field(default_factory=list)
    log_path: Path | None = None
    run_id: str = ""


@dataclass
class PendingImprovement:
    problem: str
    summary: str
    changes: list[Change]


class SelfImprover:
    def __init__(self, brain: Brain, *, root: Path | None = None,
                 log_dir: Path | None = None, verifier=None):
        self.brain = brain
        self.root = Path(root).resolve() if root else self._default_root()
        self.source_root = self.root.parent
        self.log_dir = Path(log_dir) if log_dir else self._default_log_dir()
        self._verify = verifier or self._smoke_import
        self._lock = Lock()
        self._pending: PendingImprovement | None = None

    @staticmethod
    def _default_root() -> Path:
        return Path(__file__).resolve().parent.parent

    @staticmethod
    def _default_log_dir() -> Path:
        base = os.environ.get("LOCALAPPDATA") or str(Path.home())
        return Path(base) / "FrancoV7" / "self_improve"

    _AUTONOMOUS: ClassVar[set[str]] = {
        "migliorati", "auto migliorati", "automigliorati", "migliora te stesso",
        "migliora te", "auto-migliorati", "auto miglioramento", "auto migliora", "auto",
    }

    @classmethod
    def _is_autonomous(cls, problem: str) -> bool:
        return problem.casefold().strip(" ,.!?") in cls._AUTONOMOUS

    def prepare(self, problem: str) -> str:
        """Build a reviewable plan without touching the source tree."""
        problem = (problem or "").strip()
        if not problem:
            return "Dimmi quale bug o miglioramento vuoi che risolva nel mio codice."
        if self._is_autonomous(problem):
            problem = (
                "Analizza il codice del pacchetto franco e scegli UN miglioramento "
                "concreto, sicuro e a basso rischio (bug fix, gestione errori, "
                "performance, chiarezza). Applica la modifica minima che lo realizza."
            )
        if not hasattr(self.brain, "complete"):
            return "Il cervello AI non supporta l'auto-modifica del codice."
        context = self._collect_context(problem)
        prompt = (
            f"RICHIESTA DELL'UTENTE:\n{problem}\n\n"
            f"STRUTTURA DEL PACCHETTO:\n{self._tree()}\n\n"
            f"CODICE CORRENTE (fonte di verita'):\n{context}\n\n"
            "Produci ora il JSON con la modifica minima che risolve la richiesta."
        )
        try:
            raw = self.brain.complete(prompt, system=SYSTEM_PROMPT,
                                      max_tokens=6000, temperature=.15)
        except (OSError, RuntimeError, ValueError) as exc:
            return f"Non ho potuto contattare il modello per auto-modificarmi: {exc}"
        plan = self._parse(str(raw or ""))
        if plan is None:
            plan = self._parse(self._repair(str(raw or "")))
        if plan is None:
            snippet = " ".join(str(raw or "").split())[:180]
            return ("Il modello non ha prodotto un piano di modifica valido; non ho toccato nulla."
                    + (f" Risposta: {snippet}" if snippet else ""))
        summary = str(plan.get("summary") or "").strip()
        changes = self._normalize(self._extract_changes(plan))
        if not changes:
            return summary or "Non serve alcuna modifica al mio codice."
        invalid = next((change.path for change in changes
                        if self._resolve(change.path) is None), None)
        if invalid:
            return f"Piano rifiutato: percorso non consentito: {invalid}. Non ho toccato nulla."
        with self._lock:
            self._pending = PendingImprovement(problem, summary, changes)
        files = ", ".join(dict.fromkeys(change.path for change in changes))
        understood = summary or "Ho preparato un miglioramento mirato del codice."
        return (f"Ho capito questo: {understood}\n"
                f"File previsti: {files}.\n"
                "Non ho ancora modificato nulla. Di' 'conferma miglioramento' "
                "per applicare e verificare, oppure 'annulla miglioramento'.")

    # Backwards-compatible name for callers that used the first prototype.
    def solve(self, problem: str) -> str:
        return self.prepare(problem)

    def apply_pending(self) -> str:
        """Apply the last reviewed plan, run verification and keep or roll back."""
        with self._lock:
            pending, self._pending = self._pending, None
        if pending is None:
            return "Non c'e' nessun miglioramento preparato da confermare."
        result = self._apply(pending.problem, pending.summary, pending.changes)
        return self._report(result)

    def cancel_pending(self) -> str:
        with self._lock:
            existed = self._pending is not None
            self._pending = None
        return ("Miglioramento preparato annullato; nessun file e' stato modificato."
                if existed else "Non c'e' nessun miglioramento preparato.")

    def revert_last(self) -> str:
        runs = sorted(self.log_dir.glob("run-*.json")) if self.log_dir.exists() else []
        if not runs:
            return "Non ho registrato nessun miglioramento da annullare."
        data = self._read_log(runs[-1])
        if not data:
            return "Il registro dell'ultimo miglioramento e' illeggibile."
        restored = []
        for item in data.get("changes", []):
            path = self.root / item["path"]
            original = item.get("before")
            try:
                if original is None:
                    if path.exists():
                        path.unlink()
                else:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(original, encoding="utf-8")
                restored.append(item["path"])
            except OSError:
                continue
        runs[-1].rename(runs[-1].with_suffix(".reverted"))
        if not restored:
            return "Non sono riuscito a ripristinare i file."
        return "Ho annullato l'ultimo miglioramento. File ripristinati: " + ", ".join(restored) + "."

    def _collect_context(self, problem: str) -> str:
        keywords = [k for k in re.findall(r"[A-Za-z_][A-Za-z0-9_]{2,}", problem.lower())
                    if k not in {"che", "con", "per", "del", "della", "non", "gli",
                                 "una", "uno", "the", "and", "franco"}]
        scored: list[tuple[int, Path]] = []
        for path in sorted(self.root.rglob("*.py")):
            if self._denied(path):
                continue
            try:
                if path.stat().st_size > MAX_FILE_CHARS:
                    continue
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            low = text.lower()
            score = sum(low.count(k) for k in keywords) if keywords else 0
            if path.parent == self.root / "v7":
                score += 5
            scored.append((score, path))
        scored.sort(key=lambda item: (-item[0], str(item[1])))
        parts: list[str] = []
        budget = MAX_TOTAL_CONTEXT
        for _score, path in scored:
            if budget <= 0:
                break
            rel = path.relative_to(self.root).as_posix()
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            block = f"\n### FILE {rel}\n{text}\n"
            if len(block) > budget:
                block = block[:budget] + "\n... [troncato] ...\n"
            parts.append(block)
            budget -= len(block)
        return "".join(parts)

    def _tree(self) -> str:
        lines = []
        for path in sorted(self.root.rglob("*.py")):
            if self._denied(path):
                continue
            try:
                size = path.stat().st_size
            except OSError:
                size = 0
            lines.append(f"{path.relative_to(self.root).as_posix()} ({size} byte)")
        return "\n".join(lines[:300])

    @staticmethod
    def _denied(path: Path) -> bool:
        return path.name in DENY_NAMES or bool(set(path.parts) & DENY_PARTS)

    def _repair(self, raw: str) -> str:
        if not raw.strip():
            return ""
        prompt = ("La tua risposta precedente non era un JSON valido. Ecco cosa hai scritto:\n"
                  f"{raw[:6000]}\n\n"
                  "Riscrivi ORA il solo oggetto JSON nel formato richiesto, nessun altro testo.")
        try:
            return self.brain.complete(prompt, system=SYSTEM_PROMPT,
                                       max_tokens=6000, temperature=0)
        except (OSError, RuntimeError, ValueError):
            return ""

    @staticmethod
    def _extract_changes(plan) -> list:
        if isinstance(plan, list):
            return plan
        if not isinstance(plan, dict):
            return []
        for key in _COMPLETE_KEYS:
            value = plan.get(key)
            if isinstance(value, list):
                return value
            if isinstance(value, dict):
                return [value]
        return [plan] if plan.get("path") else []

    def _parse(self, text: str) -> dict | None:
        for candidate in self._json_candidates(text):
            try:
                value = json.loads(candidate)
            except ValueError:
                continue
            if isinstance(value, list):
                return {"summary": "", "changes": value}
            if isinstance(value, dict):
                return value
        return self._parse_blocks(text)

    @staticmethod
    def _json_candidates(text: str) -> list[str]:
        candidates = []
        fence = re.search(r"```(?:json)?\s*(\{.*\}|\[.*\])\s*```", text, re.DOTALL | re.IGNORECASE)
        if fence:
            candidates.append(fence.group(1))
        for opener, closer in (("{", "}"), ("[", "]")):
            start, end = text.find(opener), text.rfind(closer)
            if start != -1 and end > start:
                candidates.append(text[start:end + 1])
        return candidates

    @staticmethod
    def _parse_blocks(text: str) -> dict | None:
        changes: list[dict] = []
        for match in re.finditer(r"```file:([^\n`]+)\n(.*?)```", text, re.DOTALL):
            changes.append({"path": match.group(1).strip(), "action": "write",
                            "content": match.group(2)})
        for match in re.finditer(r"```patch:([^\n`]+)\n(.*?)```", text, re.DOTALL):
            body = match.group(2)
            for hunk in re.finditer(r"<<<OLD\n(.*?)>>>NEW\n(.*?)(?=<<<OLD|\Z)",
                                    body, re.DOTALL):
                changes.append({"path": match.group(1).strip(), "action": "patch",
                                "old": hunk.group(1), "new": hunk.group(2)})
        if not changes:
            return None
        return {"summary": "", "changes": changes}

    def _normalize(self, raw) -> list[Change]:
        if not isinstance(raw, list):
            return []
        changes: list[Change] = []
        for item in raw[:MAX_CHANGES]:
            if not isinstance(item, dict):
                continue
            path = str(item.get("path") or "").strip()
            action = str(item.get("action") or "").strip().lower()
            if not path:
                continue
            if action in {"patch", "replace"}:
                changes.append(Change(path, "patch", old=str(item.get("old") or ""),
                                      new=str(item.get("new") or "")))
            elif action in {"write", "file", "create", "overwrite"}:
                content = str(item.get("content") or "")
                if content and len(content) <= MAX_WRITE_CHARS:
                    changes.append(Change(path, "write", content=content))
        return changes

    def _resolve(self, raw: str) -> Path | None:
        cleaned = raw.replace("\\", "/").lstrip("/")
        candidates = [cleaned]
        prefix = self.root.name + "/"
        if cleaned.startswith(prefix):
            candidates.append(cleaned[len(prefix):])
        if "/src/" + prefix in cleaned:
            candidates.append(cleaned.split("/src/" + prefix, 1)[1])
        for candidate in candidates:
            path = (self.root / candidate).resolve()
            if path == self.root or path.suffix != ".py":
                continue
            if self.root not in path.parents:
                continue
            if self._denied(path):
                continue
            return path
        return None

    def _apply(self, problem: str, summary: str, changes: list[Change]) -> RunResult:
        after: dict[Path, str] = {}
        before: dict[Path, str | None] = {}
        order: list[Path] = []
        for change in changes:
            path = self._resolve(change.path)
            if path is None:
                return RunResult("rejected", f"Percorso non consentito: {change.path}")
            if path not in after:
                try:
                    original = path.read_text(encoding="utf-8")
                except FileNotFoundError:
                    original = ""
                except OSError:
                    return RunResult("rejected", f"Non riesco a leggere {change.path}")
                after[path] = original
                before[path] = None if original == "" and not path.exists() else original
                order.append(path)
            if change.action == "write":
                after[path] = change.content if change.content.endswith("\n") else change.content + "\n"
            else:
                new_text, ok, reason = self._patch(after[path], change.old, change.new)
                if not ok:
                    return RunResult("rejected", f"Patch non applicabile su {change.path}: {reason}")
                after[path] = new_text
        for path, text in after.items():
            try:
                compile(text, str(path), "exec")
            except SyntaxError as exc:
                return RunResult("rejected", f"Il codice risultante non compila ({path.name}): {exc}")
        written: list[Path] = []
        try:
            for path in order:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(after[path], encoding="utf-8")
                written.append(path)
            ok, reason = self._verify()
        except OSError as exc:
            ok, reason = False, str(exc)
        if not ok:
            for path in written:
                original = before[path]
                try:
                    if original is None:
                        if path.exists():
                            path.unlink()
                    else:
                        path.write_text(original, encoding="utf-8")
                except OSError:
                    continue
            return RunResult("rolled_back", f"Modifica scartata e ripristinata: {reason}")
        log_path = self._write_log(problem, summary, before, after)
        return RunResult("applied", summary, [p.relative_to(self.root).as_posix() for p in order],
                         log_path)

    @staticmethod
    def _patch(original: str, old: str, new: str) -> tuple[str, bool, str]:
        if not old:
            return original, False, "testo 'old' vuoto"
        if old in original:
            return original.replace(old, new, 1), True, "ok"
        norm = lambda text: "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").split("\n"))
        if norm(old) in norm(original):
            return norm(original).replace(norm(old), new, 1), True, "ok"
        return original, False, "il testo da sostituire non e' presente nel file"

    def _smoke_import(self) -> tuple[bool, str]:
        env = dict(os.environ)
        env["PYTHONPATH"] = str(self.source_root) + os.pathsep + env.get("PYTHONPATH", "")
        code = ("import franco.v7, franco.v7.services, franco.v7.self_improve;"
                "print('ok')")
        try:
            result = subprocess.run([sys.executable, "-c", code], cwd=str(self.source_root),
                                    env=env, capture_output=True, text=True, timeout=60,
                                    check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            return False, f"verifica fallita: {exc}"
        if result.returncode != 0:
            tail = (result.stderr or result.stdout or "").strip().splitlines()[-6:]
            return False, "import rotto: " + " | ".join(tail)
        repo_root = self.source_root.parent
        test_dir = repo_root / "tests"
        tests = sorted(str(path) for path in test_dir.glob("test_v7*.py"))
        if not tests:
            return True, "compilazione e import superati"
        try:
            suite = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", *tests],
                cwd=str(repo_root), env=env, capture_output=True, text=True,
                timeout=120, check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return False, f"test V7 non completati: {exc}"
        if suite.returncode != 0:
            tail = (suite.stdout or suite.stderr or "").strip().splitlines()[-12:]
            return False, "test V7 falliti: " + " | ".join(tail)
        return True, "compilazione, import e test V7 superati"

    def _write_log(self, problem: str, summary: str, before, after) -> Path:
        self.log_dir.mkdir(parents=True, exist_ok=True)
        now = datetime.now(timezone.utc)
        stamp = now.strftime("%Y%m%d-%H%M%S")
        run_id = f"{stamp}-{os.getpid()}"
        payload = {
            "run_id": run_id,
            "ts": now.isoformat(timespec="seconds"),
            "problem": problem,
            "summary": summary,
            "changes": [
                {"path": path.relative_to(self.root).as_posix(),
                 "before": before[path], "after": after[path]}
                for path in after
            ],
        }
        log_path = self.log_dir / f"run-{run_id}.json"
        log_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return log_path

    @staticmethod
    def _read_log(path: Path) -> dict | None:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None

    @staticmethod
    def _report(result: RunResult) -> str:
        if result.status == "applied":
            files = ", ".join(result.applied)
            head = result.summary or "Ho modificato il mio codice."
            return (f"{head}\nFile aggiornati: {files}.\n"
                    "Verifica superata (compilazione, import e test V7). "
                    "Di' 'annulla l'ultimo miglioramento' per tornare indietro.")
        return result.summary
