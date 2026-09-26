"""Amber particle sphere and conversational UI for the existing pygame shell."""
from __future__ import annotations

from datetime import datetime
import json
import math
from pathlib import Path
import random
import time

try:
    import pygame
except ModuleNotFoundError:  # Headless mode keeps AI, tests and services usable.
    pygame = None
from .live_canvas import HandTracker

BG = (15, 14, 13)
PANEL = (22, 20, 18)
TEXT = (242, 237, 230)
DIM = (152, 143, 130)
AMBER = (255, 165, 65)
LINE = (53, 43, 33)


class AmberOrb:
    """Deterministic 3-D shell; motion is time based and energy follows PCM RMS."""
    def __init__(self):
        rng = random.Random(610)
        self.points = []
        for i in range(1500):
            z = 1 - 2 * (i + .5) / 1500
            a = i * math.pi * (3 - math.sqrt(5))
            s = math.sqrt(1 - z * z)
            self.points.append((s * math.cos(a), z, s * math.sin(a), rng.random()))
        self.phase = 0.0
        self.energy = 0.0
        self.previous = time.monotonic()
        self.glows = {}
        self.yaw = 0.0
        self.pitch = .25
        self.zoom = 1.0

    def glow(self, radius):
        radius = max(4, int(radius))
        if radius not in self.glows:
            surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            for r in range(radius, 0, -2):
                alpha = int(48 * (1 - r / radius) ** 2)
                pygame.draw.circle(surface, (255, 105, 16, alpha), (radius, radius), r)
            if len(self.glows) > 10:
                self.glows.clear()
            self.glows[radius] = surface
        return self.glows[radius]

    def draw(self, surface, center, radius, mode="idle", level=0.0, reduced=False):
        now = time.monotonic()
        dt = min(.1, max(0, now - self.previous))
        self.previous = now
        target = max(0, min(1, float(level or 0)))
        self.energy += (target - self.energy) * (1 - math.exp(-dt * 12))
        if not reduced:
            self.phase += dt * (.18 if mode == "thinking" else .075)
        t, energy = self.phase, self.energy
        cx, cy = map(int, center)
        radius = max(10, float(radius))
        pulse = 1 if reduced else 1 + .012 * math.sin(t * 7) + .055 * energy
        r = radius * pulse * self.zoom
        halo = self.glow(radius * 1.45)
        surface.blit(halo, (cx - halo.get_width() // 2, cy - halo.get_height() // 2))
        cosine, sine = math.cos(t + self.yaw), math.sin(t + self.yaw)
        tilt_c, tilt_s = math.cos(self.pitch), math.sin(self.pitch)

        def project(x, y, z, scale=1):
            xx, zz = x * cosine + z * sine, z * cosine - x * sine
            yy, zz = y * tilt_c - zz * tilt_s, y * tilt_s + zz * tilt_c
            perspective = 1 + zz * .13
            return (int(cx + xx * r * scale * perspective),
                    int(cy + yy * r * scale * perspective), zz)

        # Broken orbits and fine radial marks echo the reference without hiding chat.
        if radius >= 60:
            orbit = pygame.Rect(cx - int(r * 1.22), cy - int(r * 1.22),
                                int(r * 2.44), int(r * 2.44))
            for k in range(3):
                start = t * .4 + k * 2.1
                pygame.draw.arc(surface, (106, 60, 25), orbit,
                                start, start + 1.25, 1)
            for k in range(48):
                a = k * math.tau / 48
                p = (cx + math.cos(a) * r * 1.15, cy + math.sin(a) * r * 1.15)
                q = (cx + math.cos(a) * r * 1.18, cy + math.sin(a) * r * 1.18)
                pygame.draw.aaline(surface, (74, 44, 22), p, q)

        # Meridians are deliberately imperfect, like molten electrical filaments.
        for filament in range(10 if radius >= 60 else 4):
            points = []
            longitude = filament * math.pi / 5 + t * .22
            for j in range(73):
                latitude = math.tau * j / 72
                ripple = 1 + .025 * math.sin(latitude * 13 + t * 5 + filament)
                x = math.sin(latitude) * math.cos(longitude)
                y = math.cos(latitude)
                z = math.sin(latitude) * math.sin(longitude)
                px, py, depth = project(x, y, z, ripple)
                points.append((px, py))
            color = (135 + filament * 7, 64 + filament * 3, 20)
            pygame.draw.aalines(surface, color, False, points)

        fps = 60.0
        try:
            fps = float(pygame.time.get_ticks() and pygame.display.get_active() and 60 or 30)
        except Exception:
            pass
        quality_stride = 2 if fps < 40 else 1
        stride = (1 if radius >= 100 else (3 if radius >= 40 else 12)) * quality_stride
        for index in range(0, len(self.points), stride):
            x, y, z, seed = self.points[index]
            ripple = 1 + .025 * math.sin(seed * 40 + t * 6) * (1 + energy)
            px, py, depth = project(x, y, z, ripple)
            shine = (.38 + .62 * (depth + 1) / 2)
            twinkle = .75 + .25 * math.sin(t * 8 + seed * 50)
            bright = shine * twinkle
            color = (int(255 * bright), int((110 + 95 * seed) * bright),
                     int((25 + 55 * seed) * bright))
            size = 2 if radius > 100 and seed > .975 and depth > 0 else 1
            pygame.draw.circle(surface, color, (px, py), size)
            if depth > .2 and seed > .93 and radius > 60:
                ex, ey, _ = project(x, y, z, 1.10 + energy * .1)
                pygame.draw.aaline(surface, (118, 57, 19), (px, py), (ex, ey))

        # Dense golden core: interwoven rings rather than an opaque flat disc.
        for k in range(7):
            trace = []
            for j in range(65):
                a = j * math.tau / 64
                rr = r * (.12 + .025 * k) * (1 + .16 * math.sin(3 * a + t * 5 + k))
                trace.append((cx + math.cos(a + k * .45 + t) * rr,
                              cy + math.sin(a + k * .45 + t) * rr * .66))
            pygame.draw.aalines(surface, (255, 175 + k * 8, 67 + k * 12), True, trace)
        pygame.draw.circle(surface, (255, 231, 158), (cx, cy), max(1, int(r * .025)))


class OrbExperience:
    """Adapter using the existing queues, transcript, state and command engine."""
    def __init__(self, ui):
        self.ui = ui
        self.state = ui.state
        self.orb = AmberOrb()
        self.buttons = {}
        self.composer = None
        self.compact = False
        self.saved_size = (1200, 800)
        self.reduced = False
        self.wrap_cache = {}
        self.scroll_limit = 0
        self.toast = ""
        self.toast_until = 0
        self.orb_bounds = pygame.Rect(0, 0, 0, 0)
        self.orb_dragging = False
        self.orb_last_mouse = (0, 0)
        self.orb_hand = HandTracker()
        self._orb_hand_last = None
        self._orb_hand_pinched = False
        self.prefs_path = Path(__file__).resolve().parent / "franco_data" / "ui_preferences.json"
        self._load_preferences()

    def _load_preferences(self):
        try:
            prefs = json.loads(self.prefs_path.read_text(encoding="utf-8"))
        except (OSError, ValueError, TypeError):
            prefs = {}
        self.reduced = bool(prefs.get("reduced_motion", False))
        self.state.set("speech_muted", bool(prefs.get("speech_muted", False)), notify=False)
        self.state.set("voice_enabled", bool(prefs.get("voice_enabled", True)), notify=False)
        self.state.set("light_mode", bool(prefs.get("light_mode", False)), notify=False)

    def _save_preferences(self):
        self.prefs_path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.prefs_path.with_suffix(".tmp")
        temp.write_text(json.dumps({
            "reduced_motion": self.reduced,
            "speech_muted": bool(self.state.get("speech_muted", False)),
            "voice_enabled": bool(self.state.get("voice_enabled", True)),
            "light_mode": bool(self.state.get("light_mode", False)),
        }, indent=2), encoding="utf-8")
        temp.replace(self.prefs_path)

    @property
    def screen(self):
        return self.ui._screen

    def status(self):
        if self.state.get("tts_error"):
            return "error", "Voce non disponibile"
        tts = self.state.get("tts_status", "idle")
        if tts in ("loading", "restarting"):
            return "thinking", "Carico la voce XTTS"
        if tts == "synthesizing":
            return "thinking", "Preparo la risposta vocale"
        if self.state.get("speaking"):
            return "speaking", "Sto parlando"
        if self.state.get("thinking"):
            return "thinking", "Sto elaborando"
        if self.state.get("standby"):
            return "idle", "In attesa di te"
        if self.state.get("listening") and self.state.get("voice_enabled", True):
            return "listening", "Ti ascolto"
        return "idle", "Pronto a conversare"

    def text(self, text, pos, style="normal", color=TEXT, center=False):
        rendered = self.ui._txt(self.ui._fonts[style], text, color)
        self.screen.blit(rendered, (pos[0] - rendered.get_width() // 2 if center else pos[0], pos[1]))
        return rendered.get_width()

    def button(self, key, label, rect, active=False):
        rect = pygame.Rect(rect)
        self.buttons[key] = rect
        hover = rect.collidepoint(pygame.mouse.get_pos())
        color = (67, 44, 25) if active else ((49, 43, 37) if hover else (31, 28, 25))
        pygame.draw.rect(self.screen, color, rect, border_radius=10)
        pygame.draw.rect(self.screen, (139, 89, 43) if active else LINE, rect, 1, border_radius=10)
        font = self.ui._fonts["bold"]
        rendered = self.ui._txt(font, label, AMBER if active else TEXT)
        self.screen.blit(rendered, rendered.get_rect(center=rect.center))

    def header(self):
        self.buttons.clear()
        w = self.screen.get_width()
        pygame.draw.rect(self.screen, BG, (0, 0, w, 49))
        pygame.draw.line(self.screen, LINE, (0, 48), (w, 48))
        pygame.draw.circle(self.screen, AMBER, (24, 25), 4)
        self.text("FRANCO", (38, 15), "bold")
        self.text("CODE", (94, 18), "hud", AMBER)
        if w >= 940:
            self.text("OBIETTIVI AUTONOMI · VOCE LOCALE", (137, 18), "hud", DIM)
        muted = self.state.get("speech_muted", False)
        self.button("light", "Leggera", (w - 510, 8, 70, 32), self.state.get("light_mode", False))
        self.button("motion", "Animazione: " + ("ridotta" if self.reduced else "attiva"), (w - 434, 8, 144, 32))
        self.button("sound", "Voce: " + ("off" if muted else "on"), (w - 284, 8, 112, 32), not muted)
        self.button("compact", "Compatta", (w - 166, 8, 150, 32))

    def sync_window(self):
        requested = bool(self.state.get("ui_compact") or self.state.get("standby"))
        if requested == self.compact:
            return
        if requested:
            self.saved_size = self.screen.get_size()
            size = (520, 236)
        else:
            size = self.saved_size
        self.ui._screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.DOUBLEBUF)
        pygame.display.set_caption("FRANCO · Compatto" if requested else "FRANCO")
        if requested:
            try:
                from pygame._sdl2.video import Window
                window = Window.from_display_module()
                display = pygame.display.get_desktop_sizes()[0]
                window.position = (display[0] - size[0] - 18, 18)
                window.always_on_top = True
            except Exception:
                pass
        self.compact = requested
        self.buttons.clear()
        self.composer = None

    def level(self, mode):
        key = "tts_level" if mode == "speaking" else "mic_level"
        return self.state.get(key, 0) if mode in ("speaking", "listening") else 0

    def code_card(self, x, y, w, h):
        """Compact, observable status card for the autonomous goal runner."""
        card = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.screen, (25, 22, 19), card, border_radius=14)
        pygame.draw.rect(self.screen, LINE, card, 1, border_radius=14)
        code = self.state.get("franco_code", {}) or {}
        self.text("FRANCO CODE", (card.x + 14, card.y + 12), "bold", TEXT)
        if not code.get("goal"):
            pygame.draw.circle(self.screen, (99, 91, 81), (card.right - 19, card.y + 21), 4)
            self.text("Nessun obiettivo attivo", (card.x + 14, card.y + 42), "small", DIM)
            self.text("Di': Franco Code, prepara il progetto...", (card.x + 14, card.y + 67), "hud", AMBER)
            self.text("Lavorerò in background e ti aggiornerò quando serve.",
                      (card.x + 14, card.y + 88), "hud", DIM)
            return
        status = str(code.get("status", "idle"))
        status_color = ((230, 85, 66) if status == "error" else
                        (235, 177, 73) if status == "paused" else (87, 194, 125))
        pygame.draw.circle(self.screen, status_color, (card.right - 19, card.y + 21), 4)
        self.text(status.upper(), (card.right - 92, card.y + 14), "hud", status_color)
        goal_lines = self.ui._wrap(str(code.get("goal", "")), self.ui._fonts["small"], w - 28)[:2]
        for index, line in enumerate(goal_lines):
            self.text(line, (card.x + 14, card.y + 39 + index * 17), "small", TEXT)
        step = int(code.get("step", 0) or 0)
        total = max(1, int(code.get("total_steps", 0) or 1))
        phase_y = card.y + 78
        self.text(str(code.get("phase", "in attesa")), (card.x + 14, phase_y), "hud", DIM)
        self.text(f"{step}/{total}", (card.right - 42, phase_y), "hud", DIM)
        bar = pygame.Rect(card.x + 14, phase_y + 21, card.width - 28, 4)
        pygame.draw.rect(self.screen, (50, 43, 37), bar, border_radius=2)
        fill = pygame.Rect(bar.x, bar.y, int(bar.width * min(1, step / total)), bar.height)
        pygame.draw.rect(self.screen, AMBER, fill, border_radius=2)
        if status in ("running", "paused"):
            key = "code_resume" if status == "paused" else "code_pause"
            label = "Riprendi" if status == "paused" else "Pausa"
            self.button(key, label, (card.x + 14, card.bottom - 36, 86, 25), status == "paused")
            self.button("code_stop", "Ferma", (card.x + 106, card.bottom - 36, 82, 25))

    def home(self, x, y, w, h):
        self.ui._sync_chat()
        self.screen.fill(BG, (x, y, w, h))
        mode, status = self.status()
        wide = w >= 920
        if wide:
            orb_center = (x + int(w * .46), y + int(h * .43))
            radius = min(w * .32, h * .37)
            self._update_orb_hand((x, y, w, h))
            self.orb.draw(self.screen, orb_center, radius, mode, self.level(mode), self.reduced)
            self.orb_bounds = pygame.Rect(orb_center[0]-radius, orb_center[1]-radius,
                                          radius*2, radius*2)
            self.text("PRESENZA DIGITALE", (orb_center[0], y + 20), "hud", DIM, True)
            self.text(status, (orb_center[0], orb_center[1] + radius * 1.4), "bold", AMBER, True)
            self.text("XTTS / italiano", (orb_center[0], orb_center[1] + radius * 1.4 + 28), "hud", DIM, True)
            card_w = min(340, int(w * .29))
            self.code_card(x + 18, y + h - 188, card_w, 142)
            self.button("stop", "Interrompi voce", (x + 18, y + h - 38, 148, 28))
            self.text("Trascina la sfera · rotella zoom · G mani", (orb_center[0], y + h - 18), "hud", DIM, True)
        else:
            self.orb.draw(self.screen, (x + 47, y + 46), 25, mode, self.level(mode), self.reduced)
            self.text(status, (x + 90, y + 29), "bold", AMBER)
            self.text("XTTS / italiano", (x + 90, y + 53), "hud", DIM)
            self.button("stop", "Stop voce", (x + w - 130, y + 25, 112, 34))

        chat_w = min(460, max(320, int(w * .38))) if wide else max(160, w - 56)
        chat_x = x + w - chat_w - 22 if wide else x + 28
        chat_top = y + (28 if wide else 94)
        if wide:
            panel = pygame.Surface((chat_w + 20, h - 32), pygame.SRCALPHA)
            panel.fill((20, 18, 16, 218))
            pygame.draw.rect(panel, (69, 55, 42, 180), panel.get_rect(), 1, border_radius=18)
            self.screen.blit(panel, (chat_x - 10, y + 10))
            self.text("Conversazione", (chat_x, chat_top), "bold")
            self.text("Scrivi, oppure chiama Franco.", (chat_x, chat_top + 26), "normal", DIM)
            chat_top += 65
        composer_y = y + h - 106
        error = self.state.get("tts_error", "") or self.state.get("mic_error", "")
        if error:
            banner = pygame.Rect(chat_x, chat_top, chat_w, 72)
            pygame.draw.rect(self.screen, (49, 31, 22), banner, border_radius=10)
            for idx, line in enumerate(self.ui._wrap(str(error), self.ui._fonts["small"], chat_w - 22)[:3]):
                self.text(line, (chat_x + 11, chat_top + 9 + 17 * idx), "small", (255, 194, 128))
            chat_top += 84
        viewport = pygame.Rect(chat_x, chat_top, chat_w, max(20, composer_y - chat_top - 16))
        self.messages(viewport)
        self.composer = pygame.Rect(chat_x, composer_y, chat_w, 58)
        pygame.draw.rect(self.screen, (33, 29, 26), self.composer, border_radius=17)
        pygame.draw.rect(self.screen, AMBER if self.ui._input_active else LINE, self.composer, 1, border_radius=17)
        font = self.ui._fonts["input"]
        entered = self.ui._input_text
        cursor = "|" if self.ui._input_active and int(time.monotonic() * 2) % 2 == 0 else ""
        display = entered + cursor if entered or self.ui._input_active else "Messaggio a Franco..."
        while font.size(display)[0] > chat_w - 102 and len(display) > 1:
            display = display[1:]
        self.text(display, (chat_x + 17, composer_y + 21), "input", TEXT if entered else DIM)
        self.button("send", "Invia", (chat_x + chat_w - 75, composer_y + 11, 64, 36), bool(entered.strip()))
        mic_on = self.state.get("voice_enabled", True) and not self.state.get("mic_error")
        self.button("mic", "Mic: " + ("on" if mic_on else "off"), (chat_x, composer_y + 66, 94, 27), mic_on)
        device = str(self.state.get("mic_device_name", "Microfono"))
        short_device = device if len(device) <= 26 else device[:23] + "..."
        self.button("mic_cycle", short_device, (chat_x + 101, composer_y + 66, 188, 27))
        if self.state.get("mic_error"):
            self.button("mic_retry", "Riprova", (chat_x + 296, composer_y + 66, 76, 27))
        capture = self.state.get("voice_capture", {}) or {}
        hint = self.toast if time.monotonic() < self.toast_until else (
            "Sto ascoltando la frase..." if capture.get("active") else "Invio per inviare · Ctrl+M microfono")
        self.text(hint, (chat_x + 380 if chat_w > 560 else chat_x + 108, composer_y + 73), "hud", DIM)

    def _update_orb_hand(self, rect):
        if not self.orb_hand.enabled or not self.orb_hand.point:
            self._orb_hand_last = None
            return
        x, y, w, h = rect
        point = (x + self.orb_hand.point[0] * w, y + self.orb_hand.point[1] * h)
        if self.orb_hand.pinch:
            if self._orb_hand_last is not None:
                dx, dy = point[0]-self._orb_hand_last[0], point[1]-self._orb_hand_last[1]
                self.orb.yaw += dx * .012
                self.orb.pitch = max(-1.1, min(1.1, self.orb.pitch + dy * .01))
            self._orb_hand_last = point
            self._orb_hand_pinched = True
        else:
            self._orb_hand_last = None
            self._orb_hand_pinched = False
            if self.orb_hand.openness > .78:
                self.orb.zoom = min(1.45, self.orb.zoom * 1.008)
            elif self.orb_hand.openness < .32:
                self.orb.zoom = max(.65, self.orb.zoom / 1.008)

    def messages(self, viewport):
        entries = self.ui._chat_lines[-200:]
        if not entries:
            cy = viewport.centery
            self.text("Qual è il prossimo obiettivo?", (viewport.centerx, cy - 30), "large", TEXT, True)
            self.text("Parlami normalmente: posso rispondere o lavorare in background.",
                      (viewport.centerx, cy + 11), "normal", DIM, True)
            return
        prepared = []
        for role, text, stamp in entries:
            key = (str(text), viewport.width)
            if key not in self.wrap_cache:
                self.wrap_cache[key] = self.ui._wrap(str(text), self.ui._fonts["normal"], viewport.width - 46)
            lines = self.wrap_cache[key]
            prepared.append((role, lines, stamp, len(lines) * 21 + 46))
        if len(self.wrap_cache) > 250:
            self.wrap_cache.clear()
        total = sum(item[3] + 14 for item in prepared)
        self.scroll_limit = max(0, total - viewport.height)
        self.ui._chat_scroll = min(self.scroll_limit, max(0, self.ui._chat_scroll))
        draw_y = viewport.bottom - total + self.ui._chat_scroll
        old_clip = self.screen.get_clip()
        self.screen.set_clip(viewport)
        try:
            for role, lines, stamp, height in prepared:
                if draw_y + height >= viewport.top and draw_y < viewport.bottom:
                    user = str(role).upper() in ("USER", "UTENTE")
                    bubble = pygame.Rect(viewport.x + (18 if user else 0), draw_y, viewport.width - 18, height)
                    pygame.draw.rect(self.screen, (39, 34, 29) if user else PANEL, bubble, border_radius=12)
                    label = "TU" if user else "FRANCO"
                    self.text(label + "  " + str(stamp), (bubble.x + 13, draw_y + 10), "hud", DIM if user else AMBER)
                    for i, line in enumerate(lines):
                        ty = draw_y + 31 + i * 21
                        if viewport.top - 22 <= ty <= viewport.bottom:
                            self.text(line, (bubble.x + 13, ty))
                draw_y += height + 14
        finally:
            self.screen.set_clip(old_clip)

    def compact_view(self):
        self.buttons.clear()
        self.composer = None
        self.screen.fill(BG)
        w, h = self.screen.get_size()
        mode, label = self.status()
        self.orb.draw(self.screen, (40, 42), 24, mode, self.level(mode), self.reduced)
        self.text("FRANCO CODE", (78, 16), "bold")
        self.text(label, (78, 39), "small", AMBER)
        self.button("expand", "Apri", (w - 76, 12, 64, 30))
        self.button("mic", "Mic", (w - 174, 49, 48, 27), self.state.get("voice_enabled", True))
        self.button("sound", "Voce", (w - 120, 49, 50, 27), not self.state.get("speech_muted", False))
        self.button("stop", "Stop", (w - 64, 49, 52, 27))
        code = self.state.get("franco_code", {}) or {}
        if code.get("status") in ("running", "paused", "waiting_confirmation"):
            paused = code.get("status") == "paused"
            self.button("code_resume" if paused else "code_pause",
                        "Riprendi" if paused else "Pausa", (12, 82, 78, 27), paused)
            self.button("code_stop", "Ferma", (96, 82, 68, 27))
        if code.get("report_ready"):
            self.button("report", "Report", (170, 82, 70, 27), True)
        self.ui._sync_chat()
        last = self.ui._chat_lines[-1][1] if self.ui._chat_lines else "Sono qui. Apri la chat per parlare con me."
        code = self.state.get("franco_code", {}) or {}
        if code.get("goal") and code.get("status") in ("running", "paused", "error"):
            last = (f"Franco Code · {code.get('phase', '')} · "
                    f"{code.get('step', 0)}/{code.get('total_steps', 0)}\n{code.get('goal', '')}")
        last = self.state.get("tts_error") or self.state.get("mic_error") or last
        bubble = pygame.Rect(12, 91, w - 24, max(45, h - 104))
        pygame.draw.rect(self.screen, PANEL, bubble, border_radius=13)
        pygame.draw.rect(self.screen, LINE, bubble, 1, border_radius=13)
        lines = self.ui._wrap(str(last), self.ui._fonts["normal"], bubble.width - 24)
        capacity = max(1, (bubble.height - 22) // 21)
        for i, line in enumerate(lines[:capacity]):
            if i == capacity - 1 and len(lines) > capacity:
                line = line[:-3] + "..."
            self.text(line, (bubble.x + 12, bubble.y + 10 + 21 * i))

    def notify(self, message):
        self.toast, self.toast_until = message, time.monotonic() + 5

    def submit(self):
        text = self.ui._input_text.strip()
        if not text:
            return
        if len(text) > 12000:
            self.notify("Messaggio troppo lungo: massimo 12.000 caratteri.")
            return
        self.ui.command_queue.put(text)
        self.ui.transcript_buffer.append(("USER", text, datetime.now()))
        self.ui._input_text = ""
        self.ui._input_active = True
        self.ui._chat_scroll = 0

    def action(self, action):
        core = getattr(self.ui, "_franco_ref", None)
        if action == "send":
            self.submit()
        elif action in ("expand", "compact"):
            opening = action == "expand"
            self.state.set("ui_compact", not opening)
            if opening:
                self.state.set("standby", False)
                self.ui._active_section = "home"
                self.ui._input_active = True
        elif action == "motion":
            self.reduced = not self.reduced
            self._save_preferences()
        elif action == "light":
            enabled = not self.state.get("light_mode", False)
            self.state.set("light_mode", enabled, notify=False)
            self.reduced = enabled or self.reduced
            self._save_preferences()
        elif action == "sound":
            muted = not self.state.get("speech_muted", False)
            self.state.set("speech_muted", muted)
            self._save_preferences()
            if muted and core:
                core.tts.interrupt()
        elif action == "stop":
            if core:
                core.tts.interrupt()
            self.notify("Voce interrotta")
        elif action == "code_pause" and core:
            core.franco_code.pause()
        elif action == "code_resume" and core:
            core.franco_code.resume()
        elif action == "code_stop" and core:
            core.franco_code.stop()
            self.notify("Obiettivo in arresto sicuro")
        elif action == "report" and core:
            report = core.franco_code.report()
            self.ui.transcript_buffer.append(("FRANCO", report, datetime.now()))
            self.action("expand")
        elif action == "mic_cycle" and core:
            self.notify(core.voice.cycle_input_device())
        elif action == "mic_retry" and core:
            self.notify(core.voice.retry_microphone())
        elif action == "mic":
            if self.state.get("mic_error"):
                self.notify("Microfono non disponibile: puoi usare la chat.")
                return
            self.state.set("voice_enabled", not self.state.get("voice_enabled", True))
            self._save_preferences()

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            ctrl = bool(event.mod & (pygame.KMOD_CTRL | pygame.KMOD_META))
            if ctrl and event.key == pygame.K_b:
                self.action("expand" if self.compact else "compact")
                return True
            if ctrl and event.key == pygame.K_m:
                self.action("mic")
                return True
            if event.key == pygame.K_g:
                if self.orb_hand.enabled:
                    self.orb_hand.stop()
                    self.notify("Controllo gesti disattivato")
                elif self.orb_hand.start():
                    self.notify("Controllo gesti attivo")
                else:
                    self.notify(self.orb_hand.error or "Webcam/MediaPipe non disponibili")
                return True
            if event.key == pygame.K_ESCAPE and not self.ui._input_active and not self.ui._sec_input_active:
                self.action("stop")
                return True
            if self.compact and event.key == pygame.K_RETURN:
                self.action("expand")
                return True
            if self.ui._active_section == "home" and self.ui._input_active and event.key == pygame.K_RETURN:
                self.submit()
                return True
        if event.type == pygame.MOUSEWHEEL and self.ui._active_section == "home":
            if self.orb_bounds.collidepoint(pygame.mouse.get_pos()):
                self.orb.zoom = max(.65, min(1.45, self.orb.zoom * (1.06 ** event.y)))
                return True
            self.ui._chat_scroll = max(0, min(self.scroll_limit, self.ui._chat_scroll + event.y * 55))
            return True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.orb_dragging:
            self.orb_dragging = False
            return True
        if event.type == pygame.MOUSEMOTION and self.orb_dragging:
            dx, dy = event.pos[0]-self.orb_last_mouse[0], event.pos[1]-self.orb_last_mouse[1]
            self.orb.yaw += dx * .012
            self.orb.pitch = max(-1.1, min(1.1, self.orb.pitch + dy * .01))
            self.orb_last_mouse = event.pos
            return True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for action, rect in self.buttons.items():
                if rect.collidepoint(event.pos):
                    self.action(action)
                    return True
            if self.ui._active_section == "home" and self.orb_bounds.collidepoint(event.pos):
                self.orb_dragging = True
                self.orb_last_mouse = event.pos
                return True
            if self.compact:
                return True
            if self.ui._active_section == "home" and event.pos[0] > self.ui._sidebar_w:
                self.ui._input_active = bool(self.composer and self.composer.collidepoint(event.pos))
                self.ui._sec_input_active = False
                return True
        return False
