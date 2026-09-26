"""Pure audio endpointing; no device, network or model is started on import."""
from collections import deque
import math


class PhraseBuffer:
    """Keep initial consonants and pauses; bound continuous speech by duration."""
    def __init__(self, rate=16000, silence=2.2, minimum=.35, maximum=40, pre_roll=.3):
        if not (rate > 0 and all(math.isfinite(v) for v in (silence, minimum, maximum, pre_roll))
                and 0 < minimum < maximum and 0 < silence < maximum and pre_roll >= 0):
            raise ValueError("Parametri audio non validi")
        self.bytes_per_second = rate * 2
        self.silence, self.minimum, self.maximum = silence, minimum, maximum
        self.pre_roll_bytes = int(pre_roll * self.bytes_per_second)
        self.reset()

    def reset(self):
        self.active = False
        self._pre = deque()
        self._pre_size = 0
        self.data = bytearray()
        self.elapsed = self.voiced = self.quiet = 0.0

    def feed(self, chunk, voice):
        """Return one complete PCM phrase or None, independent of clock speed."""
        duration = len(chunk) / self.bytes_per_second
        if not self.active:
            if not voice:
                self._pre.append(chunk)
                self._pre_size += len(chunk)
                while self._pre and self._pre_size > self.pre_roll_bytes:
                    self._pre_size -= len(self._pre.popleft())
                return None
            self.active = True
            self.data.extend(b"".join(self._pre))
            self._pre.clear()
        self.data.extend(chunk)
        self.elapsed += duration
        if voice:
            self.voiced += duration
            self.quiet = 0.0
        else:
            self.quiet += duration
        if self.quiet >= self.silence or self.elapsed >= self.maximum:
            result = bytes(self.data) if self.voiced >= self.minimum else None
            self.reset()
            return result
        return None

    def snapshot(self):
        return {"active": self.active, "elapsed": round(self.elapsed, 1),
                "silence": round(self.quiet, 1),
                "status": "hangover" if self.quiet else "listening"}
