"""Editable real-time canvas for FRANCO CODE with optional webcam gestures."""
from __future__ import annotations

from dataclasses import dataclass, asdict
import json
import math
from pathlib import Path
import re
import threading
import time

try:
    import pygame
except ModuleNotFoundError:  # Canvas is optional in headless/server mode.
    pygame = None


COLORS = {
    "giallo": (255, 204, 62), "arancione": (255, 145, 48),
    "rosso": (235, 76, 74), "verde": (77, 193, 118),
    "blu": (68, 137, 230), "viola": (152, 103, 220),
    "bianco": (239, 235, 228), "nero": (24, 24, 24),
    "grigio": (135, 135, 135), "rosa": (236, 112, 170),
}


@dataclass
class CanvasItem:
    id: int
    kind: str
    x: float
    y: float
    w: float
    h: float
    color: tuple
    text: str = ""


class HandTracker:
    """Optional MediaPipe tracker. It never opens the camera until requested."""
    def __init__(self):
        self.available = False
        self.enabled = False
        self.error = ""
        self.point = None
        self.pinch = False
        self.openness = .5
        self._stop = threading.Event()
        self._thread = None
        try:
            import cv2  # noqa: F401
            import mediapipe  # noqa: F401
            self.available = True
        except ImportError:
            self.error = "MediaPipe non disponibile: usa mouse e tastiera"

    def start(self):
        if not self.available:
            return False
        if self._thread and self._thread.is_alive():
            self.enabled = True
            return True
        self.enabled = True
        self._stop.clear()
        self._thread = threading.Thread(target=self._run, daemon=True, name="CanvasHands")
        self._thread.start()
        return True

    def stop(self):
        self.enabled = False
        self._stop.set()

    def _run(self):
        import cv2
        import mediapipe as mp
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not capture.isOpened():
            self.error = "Webcam non disponibile"
            self.enabled = False
            return
        if not hasattr(mp, "solutions"):
            self._run_opencv(capture, cv2)
            return
        hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=.65,
                                         min_tracking_confidence=.6)
        try:
            while self.enabled and not self._stop.is_set():
                ok, frame = capture.read()
                if not ok:
                    time.sleep(.05)
                    continue
                rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
                result = hands.process(rgb)
                if not result.multi_hand_landmarks:
                    self.point, self.pinch = None, False
                    continue
                lm = result.multi_hand_landmarks[0].landmark
                index, thumb, wrist = lm[8], lm[4], lm[0]
                self.point = (index.x, index.y)
                self.pinch = math.hypot(index.x - thumb.x, index.y - thumb.y) < .045
                tips = (lm[8], lm[12], lm[16], lm[20])
                self.openness = min(1.0, sum(math.hypot(p.x-wrist.x, p.y-wrist.y)
                                             for p in tips) / 1.25)
        except Exception as error:
            self.error = str(error)
        finally:
            hands.close()
            capture.release()
            self.enabled = False

    def _run_opencv(self, capture, cv2):
        """Hand cursor fallback for MediaPipe builds without the legacy API."""
        import numpy as np
        try:
            while self.enabled and not self._stop.is_set():
                ok, frame = capture.read()
                if not ok:
                    time.sleep(.05); continue
                frame = cv2.flip(frame, 1)
                ycc = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
                mask = cv2.inRange(ycc, np.array((0, 133, 77), dtype=np.uint8),
                                   np.array((255, 173, 127), dtype=np.uint8))
                mask = cv2.medianBlur(mask, 7)
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if not contours:
                    self.point, self.pinch = None, False; continue
                contour = max(contours, key=cv2.contourArea)
                area = cv2.contourArea(contour)
                if area < 2500:
                    self.point, self.pinch = None, False; continue
                x, y, w, h = cv2.boundingRect(contour)
                top = tuple(contour[contour[:, :, 1].argmin()][0])
                self.point = (top[0] / frame.shape[1], top[1] / frame.shape[0])
                fill = area / max(1.0, w * h)
                self.openness = min(1.0, max(0.0, (1.0 - fill) * 1.8))
                self.pinch = fill > .62 and h < w * 1.35
        except Exception as error:
            self.error = "Tracciamento mano: " + str(error)
        finally:
            capture.release(); self.enabled = False


class LiveCanvas:
    def __init__(self, data_dir, logger=None):
        self.path = Path(data_dir) / "canvas_scene.json"
        self.logger = logger
        self.items = []
        self.selected = None
        self.zoom = 1.0
        self.offset = [0.0, 0.0]
        self.viewport = pygame.Rect(0, 0, 1, 1)
        self.dragging = False
        self.drag_delta = (0, 0)
        self.hand = HandTracker()
        self._last_hand_pinch = False
        self._last_zoom_at = 0.0
        self._load()

    def _load(self):
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            self.items = [CanvasItem(**{**item, "color": tuple(item["color"])}) for item in raw]
        except (OSError, ValueError, TypeError):
            self.items = []

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.path.with_suffix(".tmp")
        temp.write_text(json.dumps([asdict(item) for item in self.items], indent=2,
                                   ensure_ascii=False), encoding="utf-8")
        temp.replace(self.path)

    def _new_id(self):
        return max((item.id for item in self.items), default=0) + 1

    def _color(self, text):
        return next((value for name, value in COLORS.items() if name in text.lower()),
                    COLORS["giallo"])

    def _target(self, text):
        match = re.search(r"(?:numero|#)\s*(\d+)", text)
        if match:
            wanted = int(match.group(1))
            return next((item for item in self.items if item.id == wanted), None)
        return next((item for item in reversed(self.items) if item.id == self.selected),
                    self.items[-1] if self.items else None)

    def apply_command(self, command):
        text, low = str(command).strip(), str(command).lower().strip()
        canvas_words = ("cerchio", "rettangolo", "linea", "testo", "canvas", "tela",
                        "sposta", "ridimensiona", "elimina", "cambia colore")
        if not any(word in low for word in canvas_words):
            return None
        if any(word in low for word in ("pulisci tela", "svuota tela", "cancella tutto")):
            self.items.clear(); self.selected = None; self._save()
            return "Tela pulita."
        if low.startswith(("crea", "disegna", "aggiungi")) or "crea un" in low:
            kind = next((name for name in ("cerchio", "rettangolo", "linea", "testo")
                         if name in low), None)
            if not kind:
                return "Dimmi se vuoi un cerchio, rettangolo, linea o testo."
            item_id = self._new_id()
            label = ""
            if kind == "testo":
                quoted = re.search(r'["“](.+?)["”]', text)
                label = quoted.group(1) if quoted else re.sub(
                    r".*?testo\s+", "", text, flags=re.IGNORECASE).strip()
            sizes = [int(n) for n in re.findall(r"\b(\d{1,4})\b", low)]
            width = sizes[0] if sizes else (150 if kind != "linea" else 220)
            height = sizes[1] if len(sizes) > 1 else (width if kind == "cerchio" else 100)
            item = CanvasItem(item_id, kind, 400, 260, width, height, self._color(low), label)
            self.items.append(item); self.selected = item_id
            if len(self.items) > 500:
                self.items = self.items[-500:]
            self._save()
            return f"Ho creato {kind} numero {item_id}."
        target = self._target(low)
        if target is None:
            return "La tela è vuota. Crea prima un elemento."
        if "elimina" in low or "cancella" in low:
            self.items.remove(target); self.selected = None; self._save()
            return f"Elemento {target.id} eliminato."
        if "colore" in low or any(name in low for name in COLORS):
            target.color = self._color(low); self._save()
            return f"Colore dell'elemento {target.id} aggiornato."
        if "sposta" in low:
            amount = next((int(n) for n in re.findall(r"\d+", low)), 40)
            if "sinistra" in low: target.x -= amount
            elif "destra" in low: target.x += amount
            elif "su" in low or "alto" in low: target.y -= amount
            elif "giù" in low or "giu" in low or "basso" in low: target.y += amount
            self._save(); return f"Elemento {target.id} spostato."
        if "ridimensiona" in low or "grande" in low or "piccolo" in low:
            values = [int(n) for n in re.findall(r"\d+", low)]
            if values:
                target.w = values[0]; target.h = values[1] if len(values) > 1 else values[0]
            else:
                factor = .8 if "piccolo" in low else 1.2
                target.w *= factor; target.h *= factor
            self._save(); return f"Elemento {target.id} ridimensionato."
        return "Comando tela riconosciuto, ma manca l'azione da eseguire."

    def _world_to_screen(self, x, y):
        return (self.viewport.x + self.viewport.width / 2 + (x - 400 + self.offset[0]) * self.zoom,
                self.viewport.y + self.viewport.height / 2 + (y - 260 + self.offset[1]) * self.zoom)

    def _screen_to_world(self, x, y):
        return ((x - self.viewport.x - self.viewport.width / 2) / self.zoom + 400 - self.offset[0],
                (y - self.viewport.y - self.viewport.height / 2) / self.zoom + 260 - self.offset[1])

    def _hit(self, pos):
        wx, wy = self._screen_to_world(*pos)
        for item in reversed(self.items):
            if item.kind == "linea":
                x2, y2 = item.x + item.w, item.y + item.h
                denominator = max(1, (x2-item.x)**2 + (y2-item.y)**2)
                t = max(0, min(1, ((wx-item.x)*(x2-item.x)+(wy-item.y)*(y2-item.y))/denominator))
                if math.hypot(wx-(item.x+t*(x2-item.x)), wy-(item.y+t*(y2-item.y))) < 10/self.zoom:
                    return item
            elif item.kind == "cerchio":
                if math.hypot(wx-item.x, wy-item.y) <= item.w/2:
                    return item
            elif abs(wx-item.x) <= item.w/2 and abs(wy-item.y) <= item.h/2:
                return item
        return None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            if self.hand.enabled:
                self.hand.stop()
            else:
                self.hand.start()
            return True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.viewport.collidepoint(event.pos):
            item = self._hit(event.pos)
            self.selected = item.id if item else None
            if item:
                wx, wy = self._screen_to_world(*event.pos)
                self.drag_delta = (wx-item.x, wy-item.y); self.dragging = True
            return True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.dragging:
            self.dragging = False; self._save(); return True
        if event.type == pygame.MOUSEMOTION and self.dragging:
            item = self._target("")
            if item:
                wx, wy = self._screen_to_world(*event.pos)
                item.x, item.y = wx-self.drag_delta[0], wy-self.drag_delta[1]
            return True
        if event.type == pygame.MOUSEWHEEL and self.viewport.collidepoint(pygame.mouse.get_pos()):
            self.zoom = max(.3, min(3.0, self.zoom * (1.1 ** event.y))); return True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE and self.selected:
            item = self._target("")
            if item: self.items.remove(item); self.selected = None; self._save()
            return True
        return False

    def _update_hand(self):
        if not self.hand.enabled or not self.hand.point:
            return
        x = self.viewport.x + self.hand.point[0] * self.viewport.width
        y = self.viewport.y + self.hand.point[1] * self.viewport.height
        if self.hand.pinch:
            item = self._target("") if self._last_hand_pinch else self._hit((x, y))
            if item:
                self.selected = item.id
                wx, wy = self._screen_to_world(x, y)
                item.x, item.y = wx, wy
        elif self._last_hand_pinch:
            self._save()
        now = time.monotonic()
        if now - self._last_zoom_at > .18:
            if self.hand.openness > .78:
                self.zoom = min(3, self.zoom * 1.03); self._last_zoom_at = now
            elif self.hand.openness < .32:
                self.zoom = max(.3, self.zoom / 1.03); self._last_zoom_at = now
        self._last_hand_pinch = self.hand.pinch

    def draw(self, screen, rect, fonts):
        self.viewport = pygame.Rect(rect)
        self._update_hand()
        pygame.draw.rect(screen, (18, 17, 16), self.viewport)
        grid = max(18, int(40 * self.zoom))
        for x in range(self.viewport.x % grid, self.viewport.right, grid):
            pygame.draw.line(screen, (31, 29, 27), (x, self.viewport.y), (x, self.viewport.bottom))
        for y in range(self.viewport.y % grid, self.viewport.bottom, grid):
            pygame.draw.line(screen, (31, 29, 27), (self.viewport.x, y), (self.viewport.right, y))
        for item in self.items:
            x, y = self._world_to_screen(item.x, item.y)
            color = item.color
            selected = item.id == self.selected
            width, height = item.w*self.zoom, item.h*self.zoom
            if item.kind == "cerchio":
                pygame.draw.circle(screen, color, (int(x), int(y)), max(2, int(width/2)), 0)
            elif item.kind == "rettangolo":
                pygame.draw.rect(screen, color, (x-width/2, y-height/2, width, height), border_radius=4)
            elif item.kind == "linea":
                pygame.draw.line(screen, color, (x, y), (x+width, y+height), max(2, int(3*self.zoom)))
            elif item.kind == "testo":
                rendered = fonts["normal"].render(item.text or "Testo", True, color)
                screen.blit(rendered, (x, y))
                width, height = rendered.get_size()
            if selected:
                pygame.draw.rect(screen, (255, 174, 70), (x-width/2-5, y-height/2-5,
                                 width+10, height+10), 2, border_radius=5)
                label = fonts["hud"].render(f"#{item.id}", True, (255, 174, 70))
                screen.blit(label, (x-width/2, y-height/2-22))
        top = pygame.Rect(self.viewport.x+12, self.viewport.y+12, self.viewport.width-24, 42)
        overlay = pygame.Surface(top.size, pygame.SRCALPHA); overlay.fill((20, 18, 16, 225))
        screen.blit(overlay, top.topleft)
        title = fonts["bold"].render("CANVAS IN TEMPO REALE", True, (242, 237, 230))
        screen.blit(title, (top.x+12, top.y+12))
        hint = ("Pinch: sposta · mano aperta/chiusa: zoom · H: disattiva" if self.hand.enabled
                else "Mouse: sposta · rotella: zoom · Canc: elimina · H: mani")
        hs = fonts["hud"].render(hint, True, (151, 142, 130))
        screen.blit(hs, (top.right-hs.get_width()-12, top.y+14))
