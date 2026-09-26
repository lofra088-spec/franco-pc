"""Safe RAM monitoring and opt-in process cleanup for FRANCO.

The guard may reclaim FRANCO-owned resources automatically.  Every external
process requires a fresh, explicit confirmation and is revalidated immediately
before termination.
"""
from __future__ import annotations

import gc
import json
import os
import sys
import math
from collections import deque
from pathlib import Path
import threading
import time
from typing import Any, Dict, Iterable, List, Optional

try:
    import psutil
except Exception:  # pragma: no cover - handled as a runtime capability
    psutil = None


_SYSTEM_PROTECTED = {
    "system", "system idle process", "registry", "smss.exe", "csrss.exe",
    "wininit.exe", "services.exe", "lsass.exe", "svchost.exe", "winlogon.exe",
    "dwm.exe", "explorer.exe", "sihost.exe", "fontdrvhost.exe", "audiodg.exe",
    "securityhealthservice.exe", "securityhealthsystray.exe", "msmpeng.exe",
    "searchhost.exe", "startmenuexperiencehost.exe", "shellexperiencehost.exe",
    "taskhostw.exe", "conhost.exe", "ctfmon.exe", "runtimebroker.exe",
    "windowsterminal.exe", "powershell.exe", "pwsh.exe", "cmd.exe",
}
_UNSAVED_RISK = {
    "winword.exe", "excel.exe", "powerpnt.exe", "notepad.exe", "notepad++.exe",
    "code.exe", "devenv.exe", "photoshop.exe", "illustrator.exe", "blender.exe",
    "obsidian.exe", "libreoffice.exe", "soffice.bin", "soffice.exe",
}
_SESSION_RISK = {
    "chrome.exe", "msedge.exe", "firefox.exe", "opera.exe", "brave.exe",
    "vivaldi.exe", "arc.exe", "discord.exe", "slack.exe", "teams.exe",
    "windowsterminal.exe", "powershell.exe", "pwsh.exe", "cmd.exe",
}


class MemoryGuard:
    """Monitor memory pressure and coordinate conservative recovery actions."""

    def __init__(self, data_dir: Path, *, logger=None, state=None, event_bus=None,
                 cache=None, tts=None, warning_percent: Optional[float] = None,
                 critical_percent: Optional[float] = None):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.settings_path = self.data_dir / "memory_guard.json"
        self.report_path = self.data_dir / "memory_guard_report.jsonl"
        self.logger, self.state, self.event_bus = logger, state, event_bus
        self.cache, self.tts = cache, tts
        self.warning = float(warning_percent if warning_percent is not None else os.getenv("FRANCO_RAM_WARNING", "85"))
        self.critical = float(critical_percent if critical_percent is not None else os.getenv("FRANCO_RAM_CRITICAL", "96"))
        if not math.isfinite(self.warning) or not math.isfinite(self.critical):
            raise ValueError("Le soglie RAM devono essere numeri finiti")
        self.warning = min(98.0, max(50.0, self.warning))
        self.critical = min(99.9, max(self.warning + 1.0, self.critical))
        self._lock = threading.RLock()
        self._settings = self._load_settings()
        self._pending: Dict[str, Dict[str, Any]] = {}
        self._last_level = "normal"
        self._last_notice = 0.0

    @staticmethod
    def _key(name: str) -> str:
        key = str(name or "").strip().lower()
        return key if not key or key.endswith(".exe") else key + ".exe"

    def _load_settings(self) -> Dict[str, List[str]]:
        defaults = {"protected_apps": [], "never_suggest": []}
        try:
            data = json.loads(self.settings_path.read_text(encoding="utf-8"))
            for key in defaults:
                defaults[key] = sorted({self._key(x) for x in data.get(key, []) if x})
        except (OSError, ValueError, TypeError):
            pass
        return defaults

    def _save_settings(self) -> None:
        temp = self.settings_path.with_suffix(".tmp")
        temp.write_text(json.dumps(self._settings, ensure_ascii=False, indent=2), encoding="utf-8")
        temp.replace(self.settings_path)

    def _record(self, action: str, **details: Any) -> None:
        row = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"), "action": action, **details}
        try:
            with self.report_path.open("a", encoding="utf-8") as stream:
                stream.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
        except OSError:
            pass
        if self.logger:
            try:
                self.logger.info("MEMORY", f"{action}: {details}")
            except Exception:
                pass

    def snapshot(self) -> Dict[str, Any]:
        if psutil is None:
            return {"available": False, "percent": 0.0, "available_gb": 0.0, "level": "unknown"}
        vm = psutil.virtual_memory()
        level = "critical" if vm.percent >= self.critical else "warning" if vm.percent >= self.warning else "normal"
        return {
            "available": True,
            "percent": round(float(vm.percent), 1),
            "available_gb": round(float(vm.available) / (1024 ** 3), 2),
            "total_gb": round(float(vm.total) / (1024 ** 3), 2),
            "level": level,
            "warning_threshold": self.warning,
            "critical_threshold": self.critical,
        }

    def _iter_groups(self) -> Iterable[Dict[str, Any]]:
        if psutil is None:
            return []
        groups: Dict[str, Dict[str, Any]] = {}
        own_pid = os.getpid()
        try:
            own_children = {p.pid for p in psutil.Process(own_pid).children(recursive=True)}
        except Exception:
            own_children = set()
        try:
            this_user = psutil.Process(own_pid).username().casefold()
            own_children.update(p.pid for p in psutil.Process(own_pid).parents())
        except Exception:
            # An unreadable process owner must never become a closure candidate.
            this_user = None
        attrs = ["pid", "name", "memory_info", "create_time", "username", "exe"]
        for proc in psutil.process_iter(attrs):
            try:
                info = proc.info
                name = info.get("name") or f"PID {info['pid']}"
                key = self._key(name)
                rss = int((info.get("memory_info") or proc.memory_info()).rss)
                created = float(info.get("create_time") or time.time())
                group = groups.setdefault(key, {
                    "name": name, "key": key, "pids": [], "ram_bytes": 0,
                    "created": created, "own": False, "identities": [], "protected": False,
                })
                group["pids"].append(int(info["pid"]))
                group["ram_bytes"] += rss
                group["created"] = min(group["created"], created)
                group["own"] = group["own"] or info["pid"] == own_pid or info["pid"] in own_children
                executable = str(info.get("exe") or "").casefold()
                owner = str(info.get("username") or "").casefold()
                system_root = os.path.normcase(os.environ.get("SystemRoot", "C:\\Windows"))
                group["protected"] = group["protected"] or (
                    not this_user or owner != this_user or not executable or
                    os.path.normcase(executable).startswith(system_root + os.sep) or
                    key in _SYSTEM_PROTECTED)
                group["identities"].append({"pid": int(info["pid"]), "created": created,
                                            "exe": executable, "owner": owner})
            except (psutil.NoSuchProcess, psutil.AccessDenied, OSError):
                continue
        return groups.values()

    @staticmethod
    def _duration(seconds: float) -> str:
        seconds = max(0, int(seconds))
        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes = seconds // 60
        return f"{days}g {hours}h" if days else f"{hours}h {minutes}m" if hours else f"{minutes}m"

    def _risk(self, key: str) -> str:
        if key in _UNSAVED_RISK:
            return "potrebbe contenere lavoro non salvato"
        if key in _SESSION_RISK:
            return "potrebbe contenere sessioni o schede attive"
        return "potrebbe avere attività o lavoro non salvato; la chiusura può perderli"

    def candidates(self, limit: int = 10, include_ignored: bool = False) -> List[Dict[str, Any]]:
        protected = set(self._settings["protected_apps"])
        ignored = set(self._settings["never_suggest"])
        now = time.time()
        rows = []
        for group in self._iter_groups():
            key = group["key"]
            if group["own"] or group.get("protected") or key in _SYSTEM_PROTECTED or key in protected:
                continue
            if not include_ignored and key in ignored:
                continue
            rows.append({
                "name": group["name"], "key": key, "pids": group["pids"],
                "identities": group["identities"],
                "ram_mb": round(group["ram_bytes"] / (1024 ** 2), 1),
                "duration": self._duration(now - group["created"]),
                "warning": self._risk(key),
            })
        return sorted(rows, key=lambda x: x["ram_mb"], reverse=True)[:max(1, limit)]

    def format_candidates(self, limit: int = 8) -> str:
        rows = self.candidates(limit=limit)
        with self._lock:
            self._pending = {r["key"]: {**r, "expires": time.time() + 300} for r in rows}
        if not rows:
            return "Non vedo applicazioni suggeribili da chiudere. I processi di sistema e le app protette sono esclusi."
        lines = ["Processi che usano più memoria:"]
        for row in rows:
            lines.append(f"{row['name']} — {row['ram_mb']:.0f} MB — attivo da {row['duration']} — {row['warning']}.")
        lines.append("Per chiuderne uno scrivi: conferma chiudi seguito dal nome. La conferma scade tra 5 minuti.")
        lines.append("Puoi anche dire: proteggi app seguito dal nome, oppure non suggerire più seguito dal nome.")
        self._record("process_list_shown", count=len(rows), dry_run=True)
        return "\n".join(lines)

    def propose_close(self, name: str) -> str:
        """Prepare one external application for a later explicit confirmation."""
        key = self._key(name)
        if not key:
            return "Quale applicazione devo chiudere?"
        if key in ("franco", "franco.exe", "python", "python.exe"):
            return "Per alleggerire Franco usa il comando: ottimizza Franco."
        rows = self.candidates(limit=500, include_ignored=True)
        matches = [r for r in rows if key == r["key"]]
        if not matches:
            return f"Non trovo un'applicazione chiudibile chiamata {name}. Potrebbe essere di sistema o protetta."
        if len(matches) > 1:
            labels = ", ".join(r["name"] for r in matches[:8])
            return f"Ho trovato più corrispondenze: {labels}. Dimmi il nome esatto."
        row = matches[0]
        with self._lock:
            self._pending[row["key"]] = {**row, "expires": time.time() + 300}
        self._record("external_close_proposed", process=row, dry_run=True)
        return (f"{row['name']} usa {row['ram_mb']:.0f} MB ed è attivo da {row['duration']}. "
                f"Avviso: {row['warning']}. Per procedere scrivi: conferma chiudi {row['name']}. "
                "La conferma scade tra 5 minuti.")

    def top_summary(self, limit: int = 3) -> str:
        rows = sorted(self._iter_groups(), key=lambda x: x["ram_bytes"], reverse=True)[:limit]
        return ", ".join(f"{r['name']} {r['ram_bytes'] / (1024 ** 2):.0f} MB" for r in rows) or "nessun dato"

    def monitor_once(self) -> Optional[str]:
        snap = self.snapshot()
        if not snap["available"]:
            return None
        level = snap["level"]
        if self.state:
            self.state.update({
                "ram_percent": snap["percent"], "memory_percent": snap["percent"],
                "ram_available_gb": snap["available_gb"], "ram_level": level,
            }, notify=False)
        now = time.time()
        should_notify = level in ("warning", "critical") and (
            level != self._last_level or now - self._last_notice >= 900)
        self._last_level = level
        if not should_notify:
            return None
        self._last_notice = now
        title = "RAM critica" if level == "critical" else "RAM quasi piena"
        message = (f"{title}: {snap['percent']:.0f}% usata, {snap['available_gb']:.2f} GB disponibili. "
                   f"Processi maggiori: {self.top_summary()}. "
                   "Azioni: ottimizza Franco / mostra processi / annulla.")
        if self.state:
            self.state.set("ram_alert", {
                "level": level, "message": message,
                "actions": ["ottimizza Franco", "mostra processi", "annulla"],
                "timestamp": time.time(),
            }, notify=False)
        if self.event_bus:
            try:
                self.event_bus.emit("proactive.alert", data={
                    "message": message, "level": "danger" if level == "critical" else "warning"
                }, source="MemoryGuard")
            except Exception:
                pass
        self._record("ram_alert", **snap, top_processes=self.top_summary())
        return message

    def status_text(self) -> str:
        snap = self.snapshot()
        if not snap["available"]:
            return "Le statistiche RAM non sono disponibili."
        label = {"normal": "normale", "warning": "alta", "critical": "critica"}.get(
            snap["level"], snap["level"])
        return (f"RAM {label}: {snap['percent']:.1f}% usata, "
                f"{snap['available_gb']:.2f} GB disponibili su {snap['total_gb']:.2f} GB. "
                f"Processi maggiori: {self.top_summary()}.")

    def _cleanup_duplicate_xtts(self, dry_run: bool) -> List[str]:
        """Server lifecycle belongs to XTTSService; a name is not proof of ownership."""
        return []

    def optimize_franco(self, dry_run: bool = False) -> str:
        """Release only caches and processes that belong to this FRANCO instance."""
        before = self.snapshot()
        actions: List[str] = []
        if not dry_run:
            try:
                if self.cache is not None:
                    self.cache.clear()
                    actions.append("cache interna svuotata")
            except Exception as exc:
                self._record("self_cleanup_error", resource="cache", error=str(exc))
            try:
                if (self.tts is not None and hasattr(self.tts, "cleanup_temp_files")
                        and not (self.state and self.state.get("speaking", False))):
                    self.tts.cleanup_temp_files()
                    actions.append("audio temporaneo eliminato")
            except Exception as exc:
                self._record("self_cleanup_error", resource="tts_temp", error=str(exc))
            try:
                torch = sys.modules.get("torch")
                if torch is not None and torch.cuda.is_available():
                    torch.cuda.empty_cache()
                    actions.append("cache GPU liberata")
            except Exception:
                pass
            gc.collect()
            actions.append("oggetti inattivi liberati")
            actions.extend(self._cleanup_duplicate_xtts(dry_run=False))
            if os.name == "nt":
                try:
                    import ctypes
                    from ctypes import wintypes
                    get_handle = ctypes.windll.kernel32.GetCurrentProcess
                    get_handle.restype = wintypes.HANDLE
                    trim = ctypes.windll.psapi.EmptyWorkingSet
                    trim.argtypes = [wintypes.HANDLE]
                    if trim(get_handle()):
                        actions.append("memoria inattiva di Franco rilasciata")
                except Exception:
                    pass
        else:
            actions = ["cache interna", "audio temporaneo", "oggetti inattivi", "memoria di Franco"]
            actions.extend(self._cleanup_duplicate_xtts(dry_run=True))
        after = self.snapshot()
        # Available memory increasing means reclaimed memory.
        released = max(0.0, after.get("available_gb", 0.0) - before.get("available_gb", 0.0))
        self._record("optimize_franco", dry_run=dry_run, actions=actions,
                     before=before, after=after, released_gb=round(released, 3))
        verb = "Simulazione pronta" if dry_run else "Ottimizzazione completata"
        detail = ", ".join(actions) if actions else "nessuna risorsa inattiva trovata"
        return f"{verb}: {detail}. RAM disponibile: {after.get('available_gb', 0):.2f} GB."

    def propose_cleanup(self) -> str:
        own = self.optimize_franco(dry_run=False)
        return own + "\n" + self.format_candidates()

    def confirm_close(self, name: str, dry_run: bool = False) -> str:
        key = self._key(name)
        with self._lock:
            pending = self._pending.get(key)
            if not pending or pending.get("expires", 0) < time.time():
                return "La conferma non è valida o è scaduta. Chiedimi prima di mostrare i processi."
        current = {row["key"]: row for row in self.candidates(limit=100, include_ignored=True)}
        row = current.get(pending["key"])
        if row is None or row["key"] in _SYSTEM_PROTECTED or row["key"] in self._settings["protected_apps"]:
            return "Non posso chiudere quel processo: ora è assente, di sistema o protetto."
        previous = {p["pid"]: p for p in pending.get("identities", [])}
        identities = [p for p in row["identities"] if previous.get(p["pid"]) == p]
        if not identities or len(identities) != len(row["identities"]):
            return "L'applicazione è cambiata dopo la proposta. Mostra di nuovo i processi prima di confermare."
        if dry_run:
            self._record("external_close", dry_run=True, process=row)
            return f"Simulazione: chiuderei {row['name']} ({row['ram_mb']:.0f} MB), senza terminare nulla."
        ended, failed = [], []
        for identity in identities:
            pid = identity["pid"]
            try:
                proc = psutil.Process(pid)
                if (self._key(proc.name()) != row["key"] or
                        proc.create_time() != identity["created"] or
                        proc.exe().casefold() != identity["exe"] or
                        proc.username().casefold() != identity["owner"]):
                    continue
                proc.terminate()
                ended.append(pid)
            except (psutil.NoSuchProcess, psutil.AccessDenied, OSError) as exc:
                failed.append(f"{pid}: {exc}")
        self._record("external_close", dry_run=False, process=row, ended=ended, failed=failed)
        with self._lock:
            self._pending.pop(row["key"], None)
        if not ended:
            return f"Non sono riuscito a chiudere {row['name']}."
        suffix = f" Alcuni processi non hanno risposto: {len(failed)}." if failed else ""
        return f"Chiusura richiesta per {row['name']}.{suffix}"

    def protect(self, name: str) -> str:
        key = self._key(name)
        if not key:
            return "Dimmi quale app vuoi proteggere."
        with self._lock:
            if key not in self._settings["protected_apps"]:
                self._settings["protected_apps"].append(key)
                self._settings["protected_apps"].sort()
                self._save_settings()
        self._record("protect_app", app=key)
        return f"Ho aggiunto {name.strip()} alla lista protetta."

    def never_suggest(self, name: str) -> str:
        key = self._key(name)
        if not key:
            return "Dimmi quale app non devo più suggerire."
        with self._lock:
            if key not in self._settings["never_suggest"]:
                self._settings["never_suggest"].append(key)
                self._settings["never_suggest"].sort()
                self._save_settings()
        self._record("never_suggest", app=key)
        return f"Va bene: non suggerirò più {name.strip()}."

    def protected_list(self) -> str:
        names = self._settings["protected_apps"]
        return "App protette: " + (", ".join(names) if names else "nessuna app personalizzata") + "."

    def report(self, limit: int = 12) -> str:
        try:
            with self.report_path.open(encoding="utf-8") as stream:
                lines = list(deque(stream, maxlen=limit))
        except OSError:
            lines = []
        if not lines:
            return "Il report memoria è ancora vuoto."
        actions = []
        for line in lines:
            try:
                row = json.loads(line)
                actions.append(f"{row.get('timestamp','')} — {row.get('action','azione')}")
            except ValueError:
                continue
        return "Ultime azioni memoria:\n" + "\n".join(actions)
