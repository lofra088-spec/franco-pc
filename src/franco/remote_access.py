"""Secure, opt-in remote access for Franco.

The server binds to loopback by default. Put it behind a private VPN (for
example Tailscale) rather than exposing a raw port to the Internet.
"""
from __future__ import annotations

import base64
import json
import os
import secrets
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Callable


class RemoteAccessServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, token: str, *, screenshot: Callable[[], bytes] | None = None,
                 printer: Callable[[str], str] | None = None):
        if not token or len(token) < 24:
            raise ValueError("Il token remoto deve contenere almeno 24 caratteri")
        self.token = token
        self.screenshot = screenshot or capture_screen
        self.printer = printer or print_file
        super().__init__(("127.0.0.1", 0), _Handler)


class _Handler(BaseHTTPRequestHandler):
    server: RemoteAccessServer
    protocol_version = "HTTP/1.0"

    def log_message(self, *_args):
        return

    def _authorized(self) -> bool:
        return secrets.compare_digest(self.headers.get("Authorization", ""),
                                      f"Bearer {self.server.token}")

    def _reply(self, status: int, payload, content_type="application/json"):
        data = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if not self._authorized():
            return self._reply(401, {"error": "unauthorized"})
        if self.path == "/health":
            return self._reply(200, {"ok": True, "service": "franco-remote"})
        if self.path == "/screenshot":
            try:
                return self._reply(200, self.server.screenshot(), "image/png")
            except Exception:
                return self._reply(503, {"error": "screenshot unavailable"})
        return self._reply(404, {"error": "not found"})

    def do_POST(self):
        if not self._authorized():
            return self._reply(401, {"error": "unauthorized"})
        if self.path != "/print":
            return self._reply(404, {"error": "not found"})
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size <= 0 or size > 20 * 1024 * 1024:
                return self._reply(413, {"error": "file too large"})
            name = Path(self.headers.get("X-Filename", "document.pdf")).name
            if Path(name).suffix.lower() not in {".pdf", ".png", ".jpg", ".jpeg", ".txt"}:
                return self._reply(415, {"error": "file type not allowed"})
            target = Path(os.environ.get("FRANCO_REMOTE_PRINT_DIR", Path.cwd() / "franco_output"))
            target.mkdir(parents=True, exist_ok=True)
            path = target / name
            path.write_bytes(self.rfile.read(size))
            return self._reply(200, {"ok": True, "result": self.server.printer(str(path))})
        except Exception:
            return self._reply(400, {"error": "print request failed"})


def capture_screen() -> bytes:
    from PIL import ImageGrab
    import io
    image = ImageGrab.grab()
    output = io.BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()


def print_file(path: str) -> str:
    if os.name != "nt":
        raise RuntimeError("stampa remota disponibile su Windows")
    os.startfile(path, "print")
    return "inviato alla stampante predefinita"


def create_remote_server(token: str | None = None) -> RemoteAccessServer:
    return RemoteAccessServer(token or os.environ.get("FRANCO_REMOTE_TOKEN", ""))

