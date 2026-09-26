"""Local setup; checks never open microphones, cameras or XTTS models."""
from __future__ import annotations
import importlib
import importlib.util
import json
import math
import os
from pathlib import Path
import queue
import re
import subprocess
import sys
import tempfile
import threading
import tkinter as tk
from tkinter import messagebox, ttk

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ENV_FILE = HERE / ".env"
# Import name, distribution, user-facing label. XTTS has a separate environment.
COMPONENTS = (
    ("pygame", "pygame", "Interfaccia"),
    ("pyaudio", "PyAudio", "Microfono"),
    ("speech_recognition", "SpeechRecognition", "Riconoscimento vocale"),
    ("psutil", "psutil", "Informazioni sul PC"),
    ("dotenv", "python-dotenv", "Configurazione"),
    ("requests", "requests", "Connessioni"),
    ("numpy", "numpy", "Elaborazione audio"),
    ("sounddevice", "sounddevice", "Riproduzione audio"),
    ("openai", "openai", "Modelli AI"),
)
_KEY = re.compile(r"^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=")


def load_env(path=None):
    """Read without interpolating secrets or changing the process environment."""
    path = Path(path or ENV_FILE)
    if not path.exists():
        return {}
    try:
        from dotenv import dotenv_values
    except ImportError:
        values = {}
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            match = _KEY.match(line.strip())
            if not match:
                continue
            value = line.strip()[match.end():].strip()
            if len(value) >= 2 and value[0] == value[-1] == "'":
                value = value[1:-1].replace("\\'", "'").replace("\\\\", "\\")
            elif len(value) >= 2 and value[0] == value[-1] == '"':
                try:
                    value = json.loads(value)
                except ValueError:
                    value = value[1:-1]
            else:
                value = re.split(r"\s+#", value, maxsplit=1)[0].rstrip()
            values[match.group(1)] = value
        return values
    return {key: value or "" for key, value in dotenv_values(path, interpolate=False).items()}


def validate_values(values):
    result = {key: str(value).strip() for key, value in values.items()}
    for key, value in result.items():
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            raise ValueError("Nome dell'impostazione non valido.")
        if any(ord(char) < 32 or ord(char) == 127 for char in value):
            raise ValueError("Le impostazioni devono contenere una sola riga di testo.")
    key = result.get("OPENROUTER_API_KEY", "")
    if key and (not key.startswith("sk-or-") or any(c.isspace() for c in key)):
        raise ValueError("La chiave OpenRouter deve iniziare con sk-or- e non contenere spazi.")
    if len(key) > 512 or len(result.get("FRANCO_MIC_NAME_HINT", "")) > 160:
        raise ValueError("La chiave o il nome del microfono sono troppo lunghi.")
    try:
        warning = float(result.get("FRANCO_RAM_WARNING", "85").replace(",", "."))
        critical = float(result.get("FRANCO_RAM_CRITICAL", "96").replace(",", "."))
    except ValueError:
        raise ValueError("Inserisci due percentuali numeriche per gli avvisi RAM.") from None
    if not (math.isfinite(warning) and math.isfinite(critical) and 50 <= warning < critical <= 99.9):
        raise ValueError("Le soglie RAM devono essere in ordine crescente, tra 50 e 99,9.")
    result.update(FRANCO_RAM_WARNING=f"{warning:g}", FRANCO_RAM_CRITICAL=f"{critical:g}")
    return result


def save_env(values, path=None):
    """Preserve comments/unrelated keys, support clearing keys, replace atomically."""
    path = Path(path or ENV_FILE)
    values = validate_values(values)
    lines = path.read_text(encoding="utf-8-sig").splitlines() if path.exists() else []
    output, written = [], set()
    def setting(key):
        escaped = values[key].replace("\\", "\\\\").replace("'", "\\'")
        return f"{key}='{escaped}'"
    for line in lines:
        match = _KEY.match(line.strip())
        key = match.group(1) if match else None
        if key not in values:
            output.append(line)
        elif key not in written:
            output.append(setting(key)); written.add(key)
    output.extend(setting(key) for key in values if key not in written)
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".franco-env-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write("\n".join(output) + "\n")
            stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def inspect_runtime():
    missing = []
    for module, distribution, label in COMPONENTS:
        try:
            found = importlib.util.find_spec(module) is not None
        except (ImportError, ValueError):
            found = False
        if not found:
            missing.append((module, distribution, label))
    return {"missing": missing, "python_ok": (3, 10) <= sys.version_info[:2] < (3, 14),
            "python": ".".join(map(str, sys.version_info[:3])), "executable": sys.executable,
            "xtts_runtime": (ROOT / ".runtime" / "xtts-python" / "python.exe").is_file()}


def install_missing(missing):
    """Only invoked by the Install button. Never installs into the XTTS runtime."""
    allowed = {distribution for _, distribution, _ in COMPONENTS}
    packages = sorted({entry[1] for entry in missing} & allowed)
    if not packages:
        return 0
    env = os.environ.copy(); env["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
    # Index URLs can contain credentials, so pip output is never shown or logged.
    completed = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--no-input", *packages],
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        cwd=str(ROOT), env=env, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        timeout=1200, check=False)
    importlib.invalidate_caches()
    return completed.returncode


class Setup(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Configura FRANCO"); self.geometry("760x700"); self.minsize(620, 640)
        self.configure(bg="#111112"); self.protocol("WM_DELETE_WINDOW", self.close)
        self._jobs = queue.Queue(); self._busy = False; self._closed = False
        self._widgets = []; self._last_check = None; self._initial_error = False
        try:
            env = load_env()
        except (OSError, ValueError):
            env = {}; self._initial_error = True
        self.key = tk.StringVar(value=env.get("OPENROUTER_API_KEY", ""))
        self.mic = tk.StringVar(value=env.get("FRANCO_MIC_NAME_HINT", ""))
        self.warning = tk.StringVar(value=env.get("FRANCO_RAM_WARNING", "85"))
        self.critical = tk.StringVar(value=env.get("FRANCO_RAM_CRITICAL", "96"))
        self.status = tk.StringVar(value="Controllo i componenti installati…")
        self.details = tk.StringVar(value="")
        style = ttk.Style(self); style.theme_use("clam")
        style.configure("TFrame", background="#111112")
        style.configure("TLabel", background="#111112", foreground="#eeeeed", font=("Segoe UI", 11))
        style.configure("Hint.TLabel", foreground="#b8b2aa", font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Segoe UI Semibold", 27), foreground="#ffad55")
        style.configure("TButton", font=("Segoe UI", 10), padding=(10, 8))
        style.configure("Accent.TButton", background="#ffad55", foreground="#17120c")
        body = ttk.Frame(self, padding=(26, 22)); body.pack(fill="both", expand=True)
        ttk.Label(body, text="Benvenuto in FRANCO", style="Title.TLabel").pack(anchor="w")
        ttk.Label(body, text="Prepara il tuo assistente. Le impostazioni restano su questo PC.",
                  style="Hint.TLabel").pack(anchor="w", pady=(4, 18))
        self._field(body, "Chiave OpenRouter", self.key, secret=True)
        ttk.Label(body, text="Facoltativa se utilizzi un altro modello già configurato. La chiave resta nascosta.",
                  style="Hint.TLabel", wraplength=650).pack(anchor="w", pady=(0, 12))
        self._field(body, "Nome del microfono (facoltativo)", self.mic)
        ttk.Label(body, text="Lascia vuoto per usare il dispositivo predefinito di Windows.",
                  style="Hint.TLabel").pack(anchor="w", pady=(0, 12))
        row = ttk.Frame(body); row.pack(fill="x", pady=(0, 10))
        for label, variable in (("Avviso RAM (%)", self.warning), ("RAM critica (%)", self.critical)):
            box = ttk.Frame(row); box.pack(side="left", fill="x", expand=True, padx=(0, 14))
            self._field(box, label, variable)
        ttk.Separator(body).pack(fill="x", pady=6)
        ttk.Label(body, textvariable=self.status, wraplength=560, foreground="#ffbe7a").pack(anchor="w", pady=(10, 6))
        ttk.Label(body, textvariable=self.details, style="Hint.TLabel", wraplength=560).pack(anchor="w")
        self.progress = ttk.Progressbar(body, mode="indeterminate"); self.progress.pack(fill="x", pady=(12, 10))
        checks = ttk.Frame(body); checks.pack(fill="x")
        self._button(checks, "Controlla il PC", self.check).pack(side="left")
        self.install_button = self._button(checks, "Installa componenti mancanti", self.install)
        self.install_button.pack(side="left", padx=(10, 0))
        actions = ttk.Frame(body); actions.pack(side="bottom", fill="x", pady=(16, 0))
        self._button(actions, "Salva", self.save).pack(side="left")
        self._button(actions, "Salva e avvia FRANCO", self.launch, "Accent.TButton").pack(side="right")
        self.after(80, self._poll); self.after(100, self.check)

    def _field(self, parent, label, variable, secret=False):
        ttk.Label(parent, text=label).pack(anchor="w")
        entry = ttk.Entry(parent, textvariable=variable, show="•" if secret else "", font=("Segoe UI", 11))
        entry.pack(fill="x", pady=(4, 6), ipady=5); self._widgets.append(entry)

    def _button(self, parent, label, command, style="TButton"):
        button = ttk.Button(parent, text=label, command=command, style=style)
        self._widgets.append(button); return button

    def values(self):
        return validate_values({"OPENROUTER_API_KEY": self.key.get(), "FRANCO_MIC_NAME_HINT": self.mic.get(),
                                "FRANCO_RAM_WARNING": self.warning.get(), "FRANCO_RAM_CRITICAL": self.critical.get()})

    def _busy_state(self, busy):
        self._busy = busy
        for widget in self._widgets:
            widget.configure(state="disabled" if busy else "normal")
        if not busy:
            enabled = self._last_check and self._last_check["python_ok"] and self._last_check["missing"]
            self.install_button.configure(state="normal" if enabled else "disabled")
        self.progress.start(14) if busy else self.progress.stop()

    def _job(self, name, callback):
        if self._busy: return
        self._busy_state(True)
        def work():
            try: self._jobs.put((name, callback(), None))
            except Exception as error: self._jobs.put((name, None, type(error).__name__))
        threading.Thread(target=work, daemon=True, name="FrancoSetup").start()

    def _poll(self):
        if self._closed: return
        try:
            while True:
                name, result, error = self._jobs.get_nowait(); self._busy_state(False)
                if error:
                    self.status.set("Operazione non riuscita. Puoi riprovare.")
                    self.details.set("Controlla la connessione e l'accesso alla cartella.")
                elif name == "check": self._show_check(result)
                elif name == "install":
                    self._show_check(inspect_runtime())
                    self.status.set("Componenti installati." if result == 0 else "Installazione incompleta. Controlla Internet e riprova.")
                elif name == "launch":
                    self._show_check(result)
                    if result["python_ok"] and not result["missing"]: self._start_franco()
        except queue.Empty: pass
        self.after(100, self._poll)

    def _show_check(self, result):
        self._last_check = result; missing = result["missing"]
        if not result["python_ok"]:
            self.status.set("Ambiente Python non compatibile. Usa il collegamento di setup di FRANCO.")
        elif missing: self.status.set("Mancano alcuni componenti per avviare FRANCO.")
        else: self.status.set("Componenti principali presenti. Puoi salvare e avviare.")
        labels = ", ".join(label for _, _, label in missing)
        voice = ("Ambiente XTTS trovato; modello e voce saranno verificati all'avvio."
                 if result["xtts_runtime"] else "Ambiente XTTS assente: la chat può funzionare, la voce richiede il suo ambiente.")
        self.details.set(("Da installare: " + labels + ".\n" if labels else "") + voice + "\nI controlli non accendono microfono o webcam.")
        self._busy_state(False)
        if self._initial_error:
            self.status.set("Non riesco a leggere la configurazione precedente: verifica l'accesso alla cartella.")

    def save(self):
        if self._busy: return False
        try: save_env(self.values())
        except ValueError as error:
            messagebox.showerror("Controlla le impostazioni", str(error), parent=self); return False
        except OSError:
            messagebox.showerror("Salvataggio non riuscito", "Verifica spazio e permessi della cartella, quindi riprova.", parent=self); return False
        self._initial_error = False; self.status.set("Configurazione salvata sul PC."); return True

    def check(self):
        if not self._busy:
            self.status.set("Controllo i componenti installati…"); self._job("check", inspect_runtime)

    def install(self):
        if self._busy: return
        result = inspect_runtime()
        if not result["python_ok"] or not result["missing"]:
            self._show_check(result); return
        self.status.set("Scarico i componenti mancanti. Può richiedere alcuni minuti…")
        self.details.set("La voce XTTS mantiene il proprio ambiente. Attendi la conclusione.")
        self._job("install", lambda: install_missing(result["missing"]))

    def launch(self):
        if not self.save(): return
        self.status.set("Verifico i componenti prima di avviare…"); self._job("launch", inspect_runtime)

    def _start_franco(self):
        env = os.environ.copy()
        env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
        try:
            env.update(load_env())
            child = subprocess.Popen([sys.executable, "-m", "franco"], cwd=str(ROOT), env=env,
                stdin=subprocess.DEVNULL, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        except (OSError, ValueError):
            self.status.set("Avvio non riuscito. Le impostazioni sono state salvate."); return
        self.status.set("Avvio di FRANCO richiesto…")
        self.after(2500, lambda: self._launch_status(child))

    def _launch_status(self, child):
        if not self._closed:
            self.status.set("FRANCO è in esecuzione." if child.poll() is None else
                            "FRANCO si è chiuso all'avvio. Apri il launcher per visualizzare l'errore.")

    def close(self):
        if self._busy:
            self.status.set("Attendi la conclusione dell'operazione prima di chiudere."); return
        self._closed = True; self.destroy()


def main():
    Setup().mainloop()


if __name__ == "__main__":
    main()
