"""Loopback-only HTTP application, with no external runtime dependencies."""
from collections import deque
from datetime import date
from http import HTTPStatus
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import logging
import mimetypes
import os
from pathlib import Path
import secrets
import socket
import sqlite3
import threading
import time
from urllib.parse import parse_qs, unquote, urlsplit
import webbrowser

from .database import WorkspaceStore
from .errors import Conflict, NotFound, PayloadTooLarge, Unauthorized, WorkspaceError
from .exporting import json_bytes, note_markdown, records_csv
from .schema import RESOURCES, public_schema

LOGGER = logging.getLogger("franco.workspace")
ASSETS = Path(__file__).parent / "static"
MAX_BODY_BYTES = 16 * 1024 * 1024
MAX_JSON_DEPTH = 50


def default_data_directory():
    configured = os.environ.get("FRANCO_WORKSPACE_DATA")
    if configured:
        return Path(configured).expanduser().resolve()
    # Match the package checkout, while installed wheels use per-user storage.
    legacy = Path(__file__).resolve().parents[4]
    if (legacy / "francov6reall.py").is_file():
        return legacy / "franco_data" / "workspace"
    if os.name == "nt":
        return Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData/Local")) / "Franco" / "workspace"
    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share")) / "franco" / "workspace"


def reject_constants(value):
    raise ValueError("Numeri non finiti non ammessi")


def reject_duplicate_keys(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("Chiavi JSON duplicate")
        value[key] = item
    return value


def validate_depth(value, depth=0):
    if depth > MAX_JSON_DEPTH:
        raise WorkspaceError("JSON troppo annidato")
    if isinstance(value, dict):
        for item in value.values():
            validate_depth(item, depth + 1)
    elif isinstance(value, list):
        for item in value:
            validate_depth(item, depth + 1)


class WorkspaceServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, store):
        if address[0] != "127.0.0.1":
            raise ValueError("Workspace accetta solo l'indirizzo locale 127.0.0.1")
        self.store = store
        self.session_token = secrets.token_urlsafe(32)
        self.csrf_token = secrets.token_urlsafe(32)
        self.started_at = time.monotonic()
        self.request_times = deque(maxlen=500)
        self.metrics_lock = threading.Lock()
        super().__init__(address, WorkspaceHandler)

    @property
    def origin(self):
        return f"http://127.0.0.1:{self.server_port}"


class WorkspaceHandler(BaseHTTPRequestHandler):
    server_version = "FrancoWorkspace/1.0"
    sys_version = ""
    protocol_version = "HTTP/1.0"

    def setup(self):
        super().setup()
        self.connection.settimeout(15)

    def log_message(self, format, *args):
        # Do not put note text, search terms, cookies or query strings in logs.
        LOGGER.debug("%s %s", self.command, urlsplit(self.path).path)

    def do_GET(self):
        self._dispatch()

    def do_HEAD(self):
        self._dispatch()

    def do_POST(self):
        self._dispatch()

    def do_PATCH(self):
        self._dispatch()

    def do_DELETE(self):
        self._dispatch()

    def do_OPTIONS(self):
        self._error(Unauthorized("Le richieste cross-origin non sono consentite"))

    def _headers(self, status, content_type, length, *, extra=None):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(length))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; form-action 'self'; frame-ancestors 'none'")
        for name, value in (extra or {}).items():
            self.send_header(name, value)
        self.end_headers()

    def _send(self, body, content_type="application/json; charset=utf-8", status=200, *, extra=None):
        if not isinstance(body, bytes):
            body = json_bytes(body)
        self._headers(status, content_type, len(body), extra=extra)
        if self.command != "HEAD":
            self.wfile.write(body)

    def _error(self, error):
        try:
            self._send(error.payload(), status=error.status)
        except (BrokenPipeError, ConnectionResetError, socket.timeout):
            pass

    def _trusted_host(self):
        allowed = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        if self.headers.get("Host", "") not in allowed:
            raise Unauthorized("Host non consentito")
        fetch_site = self.headers.get("Sec-Fetch-Site")
        if fetch_site and fetch_site not in ("same-origin", "none"):
            raise Unauthorized("Apri Workspace direttamente dall'indirizzo locale")
        origin = self.headers.get("Origin")
        if origin and origin not in {f"http://{host}" for host in allowed}:
            raise Unauthorized("Origine non consentita")

    def _authenticate(self, *, mutation=False):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get("Cookie", ""))
            provided = cookie["franco_session"].value if "franco_session" in cookie else ""
        except Exception:
            provided = ""
        if not secrets.compare_digest(provided, self.server.session_token):
            raise Unauthorized("Sessione scaduta. Ricarica la pagina.")
        if mutation:
            token = self.headers.get("X-Franco-CSRF", "")
            if not secrets.compare_digest(token, self.server.csrf_token):
                raise Unauthorized("Token di sicurezza non valido. Ricarica la pagina.")

    def _body(self):
        if self.headers.get("Transfer-Encoding"):
            raise WorkspaceError("Transfer-Encoding non supportato")
        raw_length = self.headers.get("Content-Length", "0")
        try:
            length = int(raw_length)
        except ValueError:
            raise WorkspaceError("Content-Length non valido") from None
        if length < 0:
            raise WorkspaceError("Content-Length non valido")
        if length > MAX_BODY_BYTES:
            raise PayloadTooLarge("Il file supera il limite di 16 MB")
        if self.headers.get_content_type() != "application/json":
            raise WorkspaceError("Usa Content-Type: application/json")
        raw = self.rfile.read(length)
        if len(raw) != length:
            raise WorkspaceError("Richiesta incompleta")
        try:
            value = json.loads(raw.decode("utf-8"), parse_constant=reject_constants, object_pairs_hook=reject_duplicate_keys)
        except (UnicodeError, ValueError, RecursionError):
            raise WorkspaceError("JSON non valido") from None
        validate_depth(value)
        if not isinstance(value, dict):
            raise WorkspaceError("Invia un oggetto JSON")
        return value

    def _dispatch(self):
        start = time.monotonic()
        try:
            self._trusted_host()
            parsed = urlsplit(self.path)
            path = unquote(parsed.path)
            if path.startswith("/api/"):
                mutation = self.command not in ("GET", "HEAD")
                self._authenticate(mutation=mutation)
                params = parse_qs(parsed.query, keep_blank_values=True, max_num_fields=30)
                if any(len(values) != 1 for values in params.values()):
                    raise WorkspaceError("Parametri duplicati")
                self._api(path, {key: values[0] for key, values in params.items()})
            elif self.command in ("GET", "HEAD"):
                self._static(path)
            else:
                raise NotFound("Percorso non trovato")
        except WorkspaceError as exc:
            self._error(exc)
        except (BrokenPipeError, ConnectionResetError, socket.timeout):
            pass
        except sqlite3.OperationalError:
            LOGGER.exception("Database non disponibile")
            self._error(Conflict("Archivio momentaneamente occupato. Riprova tra qualche secondo."))
        except (ValueError, TypeError) as exc:
            LOGGER.debug("Richiesta non valida: %s", type(exc).__name__)
            self._error(WorkspaceError("Parametri della richiesta non validi"))
        except Exception:
            LOGGER.exception("Errore Workspace")
            error = WorkspaceError("Si è verificato un errore interno. I dati già salvati sono conservati.")
            error.status = 500
            error.code = "internal_error"
            self._error(error)
        finally:
            with self.server.metrics_lock:
                self.server.request_times.append(time.monotonic() - start)

    def _static(self, path):
        if path in ("/", "/index.html"):
            target = ASSETS / "index.html"
            extra = {"Set-Cookie": f"franco_session={self.server.session_token}; Path=/; HttpOnly; SameSite=Strict"}
        elif path.startswith("/assets/"):
            relative = path.removeprefix("/assets/")
            target = (ASSETS / relative).resolve()
            if not target.is_relative_to(ASSETS.resolve()) or not target.is_file():
                raise NotFound("Risorsa non trovata")
            extra = None
        else:
            raise NotFound("Pagina non trovata")
        if not target.is_file():
            raise NotFound("Interfaccia non trovata")
        types = {".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".html": "text/html; charset=utf-8", ".svg": "image/svg+xml"}
        content_type = types.get(target.suffix, "application/octet-stream")
        self._send(target.read_bytes(), content_type, extra=extra)

    def _api(self, path, params):
        store = self.server.store
        method = "GET" if self.command == "HEAD" else self.command
        parts = path.strip("/").split("/")[1:]
        if method == "GET" and parts == ["session"]:
            return self._send({"csrf": self.server.csrf_token, "schema": public_schema(), "settings": store.get_settings(), "version": "1.0.0"})
        if method == "GET" and parts == ["summary"]:
            return self._send(store.summary())
        if method == "GET" and parts == ["search"]:
            return self._send(store.search(params.get("q", ""), limit=params.get("limit", 40)))
        if method == "GET" and parts == ["activity"]:
            return self._send(store.activity(page=params.get("page", 1), page_size=params.get("page_size", 40)))
        if method == "GET" and parts == ["trash"]:
            return self._send(store.trash_list())
        if method == "GET" and parts == ["health"]:
            with self.server.metrics_lock:
                times = list(self.server.request_times)
            return self._send({"database": store.integrity(), "uptime_seconds": round(time.monotonic() - self.server.started_at), "recent_requests": len(times), "mean_latency_ms": round(sum(times) / len(times) * 1000, 2) if times else 0, "mode": "local", "data_directory": str(store.path.parent)})
        if parts == ["settings"]:
            if method == "GET":
                return self._send(store.get_settings())
            if method == "PATCH":
                return self._send(store.save_settings(self._body()))
        if parts == ["export"] and method == "GET":
            return self._send(store.export_bundle(), extra={"Content-Disposition": f'attachment; filename="franco-backup-{date.today().isoformat()}.json"'})
        if parts == ["import"] and method == "POST":
            return self._send(store.import_bundle(self._body()), status=201)
        if parts == ["habit-history"] and method == "GET":
            return self._send(store.habit_history(params.get("days", 35)))
        if parts == ["focus"]:
            if method == "GET":
                return self._send(store.focus_status())
            if method == "POST":
                body = self._body()
                return self._send(store.start_focus(body.get("minutes"), task_id=body.get("task_id"), label=body.get("label", "")), status=201)
        if len(parts) == 3 and parts[0] == "focus" and parts[2] == "finish" and method == "POST":
            body = self._body()
            cancel = body.get("cancel", False)
            if type(cancel) is not bool:
                raise WorkspaceError("cancel deve essere vero o falso")
            return self._send(store.finish_focus(parts[1], cancel=cancel))
        if not parts or parts[0] not in RESOURCES:
            raise NotFound("Operazione non trovata")
        resource = parts[0]
        if len(parts) == 1:
            if method == "GET":
                filters = {key[7:]: value for key, value in params.items() if key.startswith("filter.") and value != ""}
                return self._send(store.list(resource, query=params.get("q", ""), filters=filters, sort=params.get("sort", "updated_at"), direction=params.get("direction", "desc"), page=params.get("page", 1), page_size=params.get("page_size", 50), trash=params.get("trash") == "true"))
            if method == "POST":
                return self._send(store.create(resource, self._body()), status=201)
        if len(parts) == 2 and parts[1] == "export.csv" and method == "GET":
            with store.connection() as db:
                records = store.all_live(db, resource)
            return self._send(records_csv(resource, records), "text/csv; charset=utf-8", extra={"Content-Disposition": f'attachment; filename="franco-{resource}.csv"'})
        if len(parts) == 2:
            record_id = parts[1]
            if method == "GET":
                return self._send(store.get(resource, record_id))
            if method in ("PATCH", "DELETE"):
                body = self._body()
                revision = body.pop("revision", None)
                if method == "PATCH":
                    return self._send(store.update(resource, record_id, body, revision))
                if body:
                    raise WorkspaceError("Campi inattesi nella richiesta di eliminazione")
                return self._send(store.trash(resource, record_id, revision))
        if len(parts) == 3:
            record_id, action = parts[1:]
            if method == "POST" and action == "restore":
                return self._send(store.restore(resource, record_id, self._body().get("revision")))
            if method == "POST" and action == "duplicate":
                self._body()
                return self._send(store.duplicate(resource, record_id), status=201)
            if method == "POST" and action == "check" and resource == "habits":
                body = self._body()
                return self._send(store.habit_check(record_id, body.get("day"), body.get("checked")))
            if method == "GET" and action == "export.md" and resource in ("notes", "journal"):
                record = store.get(resource, record_id)
                return self._send(note_markdown(record), "text/markdown; charset=utf-8", extra={"Content-Disposition": 'attachment; filename="franco-note.md"'})
        raise NotFound("Operazione non trovata")


def serve(*, port=8787, data_directory=None, open_browser=True):
    if type(port) is not int or not 0 <= port <= 65535:
        raise ValueError("Porta non valida")
    directory = Path(data_directory) if data_directory else default_data_directory()
    store = WorkspaceStore(directory / "workspace.db")
    try:
        server = WorkspaceServer(("127.0.0.1", port), store)
    except OSError as exc:
        raise SystemExit(f"Impossibile avviare Workspace sulla porta {port}: {exc}. Prova --port 8788.") from exc
    print(f"FRANCO Workspace: {server.origin}", flush=True)
    print(f"Archivio: {store.path}", flush=True)
    print("Premi Ctrl+C per chiudere il server.", flush=True)
    if open_browser:
        threading.Timer(0.4, lambda: webbrowser.open(server.origin)).start()
    try:
        server.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        print("\nWorkspace chiuso.", flush=True)
    finally:
        server.server_close()
    return 0
