"""Transparent, always-on-top orange orb; Tk stays exclusively on its main thread."""
from __future__ import annotations

import json
import math
import os
import time
import tkinter as tk
from collections import deque
from pathlib import Path

BG = "#141311"
PANEL = "#1e1b17"
TEXT = "#f5eee4"
DIM = "#b1a494"
ORANGE = "#ff983f"
GOLD = "#ffd27a"
AMBER = "#c96724"
BRONZE = "#6f3518"
KEY_COLOR = "#010203"


def settings_path() -> Path:
    return Path(os.environ.get("LOCALAPPDATA", Path.home() / ".local/share")) / "FrancoV7" / "orb.json"


def read_settings(path: Path) -> dict:
    try:
        if path.stat().st_size > 8192:
            return {}
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


class OrbApplication:
    """A compact resident orb and one reusable conversation panel.

    Closing the panel hides it. Only Esci terminates the orb and its workers.
    No model, network, ASR or TTS calls execute from a Tk callback.
    """

    SIZE = 224

    def __init__(self, controller, *, root=None, config_path=None):
        self.controller = controller
        self.root = root or tk.Tk()
        self.config_path = Path(config_path) if config_path else settings_path()
        self.settings = read_settings(self.config_path)
        self.closed = False
        self.panel_visible = False
        self._timers = set()
        self._messages = deque(maxlen=80)
        self._start = time.monotonic()
        self._drag = None
        self._status = "Pronto · microfono spento"
        self._busy = False
        self._mic = False
        self._voice = True
        self._reduced = bool(self.settings.get("reduced_motion", False))
        self.root.withdraw()
        self.root.title("Franco V7 · Sfera")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg=KEY_COLOR)
        self.transparent = False
        if os.name == "nt":
            self.root.attributes("-transparentcolor", KEY_COLOR)
            self.root.attributes("-toolwindow", True)
            self.transparent = True
        x, y = self._initial_position()
        self.root.geometry(f"{self.SIZE}x{self.SIZE + 25}+{x}+{y}")
        self.canvas = tk.Canvas(self.root, width=self.SIZE, height=self.SIZE + 25,
                                bg=KEY_COLOR, highlightthickness=0, cursor="hand2")
        self.canvas.pack(fill="both", expand=True)
        self._build_orb()
        self._build_panel()
        self._build_menu()
        self.canvas.bind("<ButtonPress-1>", self._press)
        self.canvas.bind("<B1-Motion>", self._move)
        self.canvas.bind("<ButtonRelease-1>", self._release)
        self.canvas.bind("<Button-3>", self._popup)
        self.root.bind("<Return>", lambda _: self.toggle_panel())
        self.root.bind("<space>", lambda _: self.toggle_panel())
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        if self.settings.get("voice_muted"):
            self.controller.toggle_voice()
        self._update_controls()
        self.root.deiconify()
        self._later(0, self._animate)
        self._later(40, self._poll)

    def _initial_position(self):
        width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        try:
            x = int(self.settings.get("x", width - self.SIZE - 35))
            y = int(self.settings.get("y", height - self.SIZE - 110))
        except (TypeError, ValueError):
            x, y = width - self.SIZE - 35, height - self.SIZE - 110
        return max(0, min(x, width - self.SIZE)), max(0, min(y, height - self.SIZE - 60))

    def _later(self, delay, callback):
        if self.closed:
            return
        token = None
        def fire():
            self._timers.discard(token)
            if not self.closed:
                callback()
        token = self.root.after(delay, fire)
        self._timers.add(token)

    def _build_orb(self):
        c = self.SIZE / 2
        # Layered HUD geometry inspired by the supplied orange energy sphere.
        # Everything remains native Canvas geometry: no large texture, GPU or
        # neural model is held in memory while the orb is resident.
        self._hud = []
        for inset, color in ((9, BRONZE), (18, "#8a421d")):
            length = 30 if inset == 9 else 18
            corners = (
                (inset, inset, inset + length, inset),
                (inset, inset, inset, inset + length),
                (self.SIZE-inset, inset, self.SIZE-inset-length, inset),
                (self.SIZE-inset, inset, self.SIZE-inset, inset+length),
                (inset, self.SIZE-inset, inset+length, self.SIZE-inset),
                (inset, self.SIZE-inset, inset, self.SIZE-inset-length),
                (self.SIZE-inset, self.SIZE-inset, self.SIZE-inset-length, self.SIZE-inset),
                (self.SIZE-inset, self.SIZE-inset, self.SIZE-inset, self.SIZE-inset-length),
            )
            self._hud.extend(self.canvas.create_line(*coords, fill=color, width=1)
                             for coords in corners)
        self._hud.extend([
            self.canvas.create_line(18, 38, 80, 38, fill=AMBER, width=2),
            self.canvas.create_line(self.SIZE-72, self.SIZE-28, self.SIZE-18,
                                    self.SIZE-28, fill=AMBER, width=2),
            self.canvas.create_line(25, self.SIZE-20, 50, self.SIZE-20,
                                    fill=BRONZE, width=1),
        ])
        self._halos = [
            self.canvas.create_oval(c-rx, c-ry, c+rx, c+ry, outline=color, width=width)
            for rx, ry, color, width in (
                (92, 92, "#3f2418", 1), (82, 88, BRONZE, 1),
                (73, 82, "#8a421d", 1), (57, 66, "#b05a25", 1),
            )
        ]
        self._arcs = []
        for index, (radius, extent, width, color) in enumerate((
            (94, 44, 1, BRONZE), (87, 72, 2, AMBER), (78, 38, 1, ORANGE),
            (70, 96, 2, "#e77c2f"), (60, 58, 1, GOLD), (48, 120, 2, ORANGE),
        )):
            self._arcs.append(self.canvas.create_arc(
                c-radius, c-radius, c+radius, c+radius, style="arc", outline=color,
                width=width, extent=extent, start=index*57,
            ))
        self._ticks = []
        for index in range(56):
            angle = index * math.tau / 56
            inner = 78 + (index % 5 == 0) * -5
            outer = 83 + (index % 7 == 0) * 7
            self._ticks.append(self.canvas.create_line(
                c + math.cos(angle)*inner, c + math.sin(angle)*inner,
                c + math.cos(angle)*outer, c + math.sin(angle)*outer,
                fill=AMBER if index % 5 == 0 else BRONZE,
                width=2 if index % 7 == 0 else 1,
            ))
        self._points = []
        point_count = 360
        for i in range(point_count):
            z = 1 - 2 * (i + .5) / point_count
            angle = i * math.pi * (3 - math.sqrt(5))
            radius = math.sqrt(1 - z*z)
            point = (radius * math.cos(angle), z, radius * math.sin(angle))
            item = self.canvas.create_oval(0, 0, 2, 2, fill=ORANGE, outline="")
            self._points.append((point, item))
        self._filaments = [self.canvas.create_line(0, 0, 0, 0, fill=AMBER, width=1)
                           for _ in range(42)]
        self._core_glow = self.canvas.create_oval(c-22, c-22, c+22, c+22,
                                                  outline=AMBER, width=2)
        self._core_ring = self.canvas.create_oval(c-13, c-13, c+13, c+13,
                                                  outline=ORANGE, width=2)
        self._core = self.canvas.create_oval(c-5, c-5, c+5, c+5,
                                             fill=GOLD, outline="#fff0bd")
        self._badge = self.canvas.create_text(c, self.SIZE + 9, text="FRANCO",
                                               fill=ORANGE,
                                               font=("Cascadia Mono", 9, "bold"))

    def _animate(self):
        t = 0 if self._reduced else time.monotonic() - self._start
        c = self.SIZE / 2
        rotation = t * (.65 if self._busy else .17)
        cosine, sine = math.cos(rotation), math.sin(rotation)
        radius = 72 * (1 + .025 * math.sin(t * 2.2))
        projected = []
        for (x, y, z), item in self._points:
            px, depth = x*cosine + z*sine, z*cosine - x*sine
            py = y*.92 - depth*.27
            perspective = 1 + depth*.12
            sx, sy = c + px*radius*perspective, c + py*radius*perspective
            size = 1.4 if depth > 0 else .85
            brightness = .45 + .55*(depth+1)/2
            red = int(255*brightness)
            green = int((116 + (depth+1)*32)*brightness)
            blue = int(35*brightness)
            color = f"#{red:02x}{green:02x}{blue:02x}"
            self.canvas.coords(item, sx-size, sy-size, sx+size, sy+size)
            self.canvas.itemconfigure(item, fill=color)
            projected.append((sx, sy, depth))
        for index, line in enumerate(self._filaments):
            first = projected[(index*7 + int(t*4)) % len(projected)]
            second = projected[(index*19 + 83 + int(t*3)) % len(projected)]
            if first[2] + second[2] > -.15:
                self.canvas.coords(line, first[0], first[1], second[0], second[1])
                self.canvas.itemconfigure(line, state="normal",
                                          fill=GOLD if index % 7 == 0 else AMBER)
            else:
                self.canvas.itemconfigure(line, state="hidden")
        for i, arc in enumerate(self._arcs):
            direction = -1 if i % 2 else 1
            self.canvas.itemconfigure(arc, start=(direction*t*(18+i*3)+i*57)%360)
        pulse = 16 + 5 * (.5 + .5*math.sin(t*3.1))
        self.canvas.coords(self._core_glow, c-pulse, c-pulse, c+pulse, c+pulse)
        knot = 8 + 3 * (.5 + .5*math.cos(t*4.3))
        self.canvas.coords(self._core_ring, c-knot, c-knot, c+knot, c+knot)
        self._later(250 if self._reduced else (40 if self._busy or self._mic else 80), self._animate)

    def _button(self, parent, text, command, *, accent=False):
        return tk.Button(parent, text=text, command=command, font=("Segoe UI", 10),
                         fg=BG if accent else TEXT, bg=ORANGE if accent else PANEL,
                         activebackground="#ffa951", activeforeground=BG, relief="flat",
                         borderwidth=0, padx=12, pady=9, cursor="hand2", takefocus=True)

    def _build_panel(self):
        self.panel = tk.Toplevel(self.root)
        self.panel.withdraw()
        self.panel.title("Franco V7 · Conversazione")
        self.panel.configure(bg=BG)
        self.panel.minsize(640, 500)
        self.panel.protocol("WM_DELETE_WINDOW", self.hide_panel)
        self.panel.bind("<Escape>", lambda _: self.hide_panel())
        self.panel.columnconfigure(0, weight=1)
        self.panel.rowconfigure(2, weight=1)
        header = tk.Frame(self.panel, bg=BG)
        header.grid(row=0, column=0, sticky="ew", padx=22, pady=(20, 8))
        tk.Label(header, text="FRANCO", font=("Segoe UI", 20, "bold"), fg=ORANGE, bg=BG).pack(side="left")
        self._button(header, "Torna alla sfera", self.hide_panel).pack(side="right")
        self._button(header, "Impostazioni", lambda: self._show_screen("settings")).pack(side="right", padx=4)
        self._button(header, "Mappa e fonti", lambda: self._show_screen("intel")).pack(side="right", padx=4)
        self._button(header, "Chat", lambda: self._show_screen("chat"), accent=True).pack(side="right", padx=4)
        self.status_var = tk.StringVar(value=self._status)
        self.status_label = tk.Label(self.panel, textvariable=self.status_var, anchor="w", fg=DIM, bg=BG,
                                     font=("Segoe UI", 10), wraplength=445)
        self.status_label.grid(row=1, column=0, sticky="ew", padx=22, pady=(0, 14))
        frame = tk.Frame(self.panel, bg=BG)
        frame.grid(row=2, column=0, sticky="nsew", padx=20)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        self.transcript = tk.Text(frame, bg=BG, fg=TEXT, font=("Segoe UI", 11), wrap="word",
                                  relief="flat", borderwidth=0, padx=6, pady=8, state="disabled",
                                  exportselection=False, cursor="arrow")
        self.transcript.grid(row=0, column=0, sticky="nsew")
        scrollbar = tk.Scrollbar(frame, command=self.transcript.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.transcript.configure(yscrollcommand=scrollbar.set)
        for name, color in (("user", DIM), ("assistant", ORANGE), ("system", "#d8af7a")):
            self.transcript.tag_configure(name, foreground=color, font=("Segoe UI", 9, "bold"), spacing1=16, spacing3=5)
        self.transcript.tag_configure("body", spacing3=12)
        self.partial_var = tk.StringVar(value="")
        self.partial_label = tk.Label(self.panel, textvariable=self.partial_var, fg=DIM, bg=BG,
                                      anchor="w", justify="left", wraplength=440,
                                      font=("Segoe UI", 10, "italic"))
        self.partial_label.grid(row=3, column=0, sticky="ew", padx=24, pady=7)
        controls = tk.Frame(self.panel, bg=BG)
        controls.grid(row=4, column=0, sticky="ew", padx=22, pady=(6, 12))
        self.mic_button = self._button(controls, "Accendi microfono", self.toggle_microphone)
        self.mic_button.pack(side="left", padx=(0, 8))
        self.voice_button = self._button(controls, "Muta Franco", self.toggle_voice)
        self.voice_button.pack(side="left")
        self.stop_button = self._button(controls, "Interrompi", self.controller.cancel)
        self.stop_button.pack(side="right")
        composer = tk.Frame(self.panel, bg=PANEL, padx=12, pady=10)
        composer.grid(row=5, column=0, sticky="ew", padx=22, pady=(0, 10))
        composer.columnconfigure(0, weight=1)
        self.entry = tk.Entry(composer, bg=PANEL, fg=TEXT, insertbackground=ORANGE,
                               relief="flat", font=("Segoe UI", 11))
        self.entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.entry.bind("<Return>", self._send)
        self.send_button = self._button(composer, "Invia", self._send, accent=True)
        self.send_button.grid(row=0, column=1)
        footer = tk.Frame(self.panel, bg=BG)
        footer.grid(row=6, column=0, sticky="ew", padx=22, pady=(0, 15))
        tk.Label(footer, text="Chiudi la chat: la sfera resta disponibile.", font=("Segoe UI", 9), bg=BG, fg=DIM).pack(side="left")
        self._button(footer, "Esci", self.close).pack(side="right")
        self._chat_widgets = [self.status_label, frame, self.partial_label,
                              controls, composer, footer]
        self._build_extra_screens()
        self._append("system", "Scrivi qui oppure accendi il microfono. Puoi silenziare la voce di Franco e continuare a leggere le risposte.")

    def _build_extra_screens(self):
        self.intel_page = tk.Frame(self.panel, bg=BG)
        self.intel_page.columnconfigure(0, weight=1)
        tk.Label(self.intel_page, text="MAPPA E FONTI PUBBLICHE", fg=ORANGE, bg=BG,
                 font=("Segoe UI", 15, "bold")).grid(row=0, column=0, sticky="w", pady=(16, 8))
        tk.Label(self.intel_page,
                 text="Argos Atlas per mappa, telecamere e voli. Max Intel e fonti enciclopediche per ricerche pubbliche e legali.",
                 fg=DIM, bg=BG, justify="left", wraplength=440,
                 font=("Segoe UI", 10)).grid(row=1, column=0, sticky="ew", pady=(0, 18))
        self.place_entry = self._screen_entry(self.intel_page, "Citta o zona")
        self.place_entry.grid(row=2, column=0, sticky="ew", pady=5)
        place_actions = tk.Frame(self.intel_page, bg=BG)
        place_actions.grid(row=3, column=0, sticky="w", pady=(4, 18))
        self._button(place_actions, "Telecamere", lambda: self._send_template(
            "mostrami le telecamere di {}", self.place_entry)).pack(side="left", padx=(0, 7))
        self._button(place_actions, "Voli", lambda: self._send_template(
            "mostrami tutti i voli sopra {}", self.place_entry)).pack(side="left", padx=(0, 7))
        self._button(place_actions, "Mappa mondo", lambda: self._submit_command(
            "Franco mappa")).pack(side="left")
        self.person_entry = self._screen_entry(self.intel_page, "Nome pubblico da verificare")
        self.person_entry.grid(row=4, column=0, sticky="ew", pady=5)
        self._button(self.intel_page, "Ricerca persona con fonti", lambda: self._send_template(
            "cerca una persona {}", self.person_entry), accent=True).grid(row=5, column=0, sticky="w", pady=(4, 18))
        self._button(self.intel_page, "Geolocalizza una foto con GeoSpy",
                     self._choose_image).grid(row=6, column=0, sticky="w")
        tk.Label(self.intel_page,
                 text="Franco non raccoglie indirizzi, telefoni, credenziali o posizione privata. Le stime visive non sono prove.",
                 fg="#d8af7a", bg=BG, justify="left", wraplength=440,
                 font=("Segoe UI", 9)).grid(row=7, column=0, sticky="ew", pady=(22, 0))

        self.settings_page = tk.Frame(self.panel, bg=BG)
        tk.Label(self.settings_page, text="IMPOSTAZIONI", fg=ORANGE, bg=BG,
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=(16, 18))
        tk.Label(self.settings_page, text="Microfono e voce sono controlli indipendenti.",
                 fg=TEXT, bg=BG, font=("Segoe UI", 11)).pack(anchor="w", pady=(0, 12))
        self._button(self.settings_page, "Accendi / spegni microfono",
                     self.toggle_microphone).pack(anchor="w", pady=5)
        self._button(self.settings_page, "Muta / attiva voce Franco",
                     self.toggle_voice).pack(anchor="w", pady=5)
        self._button(self.settings_page, "Riduci / attiva animazione",
                     self.toggle_animation).pack(anchor="w", pady=5)
        tk.Label(self.settings_page,
                 text="L'elaborazione parziale prepara l'intento mentre parli, ma nessun comando parte prima della fine della frase.",
                 fg=DIM, bg=BG, justify="left", wraplength=440,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(22, 0))

    def _screen_entry(self, parent, placeholder):
        entry = tk.Entry(parent, bg=PANEL, fg=TEXT, insertbackground=ORANGE,
                         relief="flat", font=("Segoe UI", 11))
        entry.insert(0, placeholder)
        entry._franco_placeholder = placeholder
        entry.bind("<FocusIn>", lambda _e, w=entry, p=placeholder:
                   w.delete(0, "end") if w.get() == p else None)
        return entry

    def _show_screen(self, name):
        self.intel_page.grid_remove()
        self.settings_page.grid_remove()
        for widget in self._chat_widgets:
            widget.grid_remove()
        if name == "chat":
            for widget in self._chat_widgets:
                widget.grid()
            self.entry.focus_set()
        else:
            page = self.intel_page if name == "intel" else self.settings_page
            page.grid(row=1, column=0, rowspan=6, sticky="nsew", padx=24, pady=(0, 18))

    def _submit_command(self, text):
        if self.controller.submit(text):
            self._show_screen("chat")

    def _send_template(self, template, entry):
        value = entry.get().strip()
        if value and value != getattr(entry, "_franco_placeholder", ""):
            self._submit_command(template.format(value))

    def _choose_image(self):
        from tkinter import filedialog
        path = filedialog.askopenfilename(
            parent=self.panel, title="Scegli una foto",
            filetypes=[("Immagini", "*.jpg *.jpeg *.png *.webp")])
        if path:
            self._submit_command(f'geolocalizza questa foto "{path}"')

    def _build_menu(self):
        self.menu = tk.Menu(self.root, tearoff=False, bg=PANEL, fg=TEXT)
        self.menu.add_command(label="Apri conversazione", command=self.show_panel)
        self.menu.add_command(label="Accendi / spegni microfono", command=self.toggle_microphone)
        self.menu.add_command(label="Muta / attiva voce Franco", command=self.toggle_voice)
        self.menu.add_command(label="Interrompi risposta", command=self.controller.cancel)
        self.menu.add_separator()
        self.menu.add_command(label="Riduci / attiva animazione", command=self.toggle_animation)
        self.menu.add_command(label="Esci da Franco", command=self.close)

    def _popup(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def _press(self, event):
        self._drag = (event.x_root, event.y_root, self.root.winfo_x(), self.root.winfo_y(), False)

    def _move(self, event):
        if not self._drag:
            return
        x, y, wx, wy, moved = self._drag
        dx, dy = event.x_root-x, event.y_root-y
        if moved or dx*dx+dy*dy > 36:
            self._drag = (x, y, wx, wy, True)
            nx = max(0, min(wx+dx, self.root.winfo_screenwidth()-self.SIZE))
            ny = max(0, min(wy+dy, self.root.winfo_screenheight()-self.SIZE-60))
            self.root.geometry(f"+{nx}+{ny}")

    def _release(self, _event):
        if self._drag and not self._drag[-1]:
            self.toggle_panel()
        self._drag = None

    def toggle_panel(self):
        self.hide_panel() if self.panel_visible else self.show_panel()

    def show_panel(self):
        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        w, h = min(760, sw-30), min(690, sh-70)
        x = max(10, min(self.root.winfo_x()-w-12, sw-w-10))
        y = max(10, min(self.root.winfo_y()-h+100, sh-h-45))
        self.panel.geometry(f"{w}x{h}+{x}+{y}")
        self.panel.deiconify()
        self.panel.lift()
        self.panel_visible = True
        self.entry.focus_set()

    def hide_panel(self):
        self.panel.withdraw()
        self.panel_visible = False

    def toggle_microphone(self):
        self.controller.toggle_microphone()
        self._update_controls()

    def toggle_voice(self):
        self.controller.toggle_voice()
        self._update_controls()

    def toggle_animation(self):
        self._reduced = not self._reduced

    def _send(self, _event=None):
        text = self.entry.get().strip()
        if text and self.controller.submit(text):
            self.entry.delete(0, "end")
        self._update_controls()
        return "break"

    def _append(self, role, text):
        text = str(text)[:24000]
        self._messages.append((role, text))
        at_bottom = self.transcript.yview()[1] >= .98
        self.transcript.configure(state="normal")
        # Bounded transcript: rebuilding happens only on messages, never frames.
        self.transcript.delete("1.0", "end")
        for speaker, body in self._messages:
            label = {"user": "TU", "assistant": "FRANCO", "system": "STATO"}.get(speaker, "STATO")
            self.transcript.insert("end", label+"\n", speaker)
            self.transcript.insert("end", body+"\n", "body")
        self.transcript.configure(state="disabled")
        if at_bottom:
            self.transcript.see("end")

    def _update_controls(self):
        self._mic = self.controller.microphone_enabled
        self._voice = self.controller.voice_enabled
        self._busy = self.controller.busy
        self.mic_button.configure(text="Muta microfono" if self._mic else "Accendi microfono")
        self.voice_button.configure(text="Muta Franco" if self._voice else "Attiva voce Franco")
        self.send_button.configure(state="disabled" if self._busy else "normal")
        self.stop_button.configure(state="normal" if self._busy else "disabled")
        label = "ELABORO" if self._busy else ("ASCOLTO" if self._mic else "MIC SPENTO")
        if not self._voice:
            label += " · MUTO"
        self.canvas.itemconfigure(self._badge, text=label)

    def _poll(self):
        for event in self.controller.drain_events():
            kind = event.get("type")
            if kind == "message":
                self._append(event.get("role", "system"), event.get("text", ""))
            elif kind == "error":
                self._append("system", event.get("text", "Operazione non riuscita."))
            elif kind == "partial":
                self.partial_var.set(str(event.get("text", ""))[-220:])
            elif kind == "state":
                self._status = str(event.get("status", self._status))
        self.status_var.set(self._status)
        self._update_controls()
        self._later(40, self._poll)

    def close(self):
        if self.closed:
            return
        self.closed = True
        self.controller.close()
        try:
            settings = {"x": self.root.winfo_x(), "y": self.root.winfo_y(),
                        "voice_muted": not self._voice, "reduced_motion": self._reduced}
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.config_path.with_suffix(".tmp")
            tmp.write_text(json.dumps(settings), encoding="utf-8")
            tmp.replace(self.config_path)
        except OSError:
            pass
        for token in self._timers:
            try:
                self.root.after_cancel(token)
            except tk.TclError:
                pass
        self._timers.clear()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


def run_desktop(runtime):
    from .desktop_controller import DesktopController
    from .desktop_voice import DesktopMicrophone, DesktopSpeech
    controller = DesktopController(runtime, speech=DesktopSpeech, microphone=DesktopMicrophone)
    try:
        OrbApplication(controller).run()
    finally:
        controller.close()
    return 0
