"""SQLite repository for the standalone FRANCO workspace.

Each operation opens a short-lived connection. Mutations use BEGIN IMMEDIATE,
optimistic revisions, and an activity entry in the same transaction. A failed
mutation therefore never leaves a partial write or a misleading activity event.
"""
from contextlib import contextmanager
from copy import deepcopy
from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3
import threading
import uuid

from .errors import Conflict, NotFound, WorkspaceError
from .schema import RESOURCES, SETTINGS
from .validation import positive_int, validate_consistency, validate_record


def timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


class WorkspaceStore:
    SCHEMA_VERSION = 1
    EXPORT_VERSION = 1
    MAX_IMPORT_RECORDS = 20000

    def __init__(self, path):
        self.path = Path(path).resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_lock = threading.Lock()
        self._initialize()

    @contextmanager
    def connection(self, *, write=False):
        connection = sqlite3.connect(self.path, timeout=15, isolation_level=None)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("PRAGMA busy_timeout=15000")
        try:
            if write:
                connection.execute("BEGIN IMMEDIATE")
            yield connection
            if write:
                connection.commit()
        except BaseException:
            if connection.in_transaction:
                connection.rollback()
            raise
        finally:
            connection.close()

    def _initialize(self):
        with self._init_lock, self.connection() as db:
            db.execute("PRAGMA journal_mode=WAL")
            version = db.execute("PRAGMA user_version").fetchone()[0]
            if version > self.SCHEMA_VERSION:
                raise WorkspaceError("La base dati proviene da una versione più recente di FRANCO")
            db.executescript("""
                BEGIN IMMEDIATE;
                CREATE TABLE IF NOT EXISTS records (
                    id TEXT PRIMARY KEY,
                    resource TEXT NOT NULL,
                    payload TEXT NOT NULL,
                    title TEXT NOT NULL,
                    search_text TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    deleted_at TEXT,
                    revision INTEGER NOT NULL DEFAULT 1
                );
                CREATE INDEX IF NOT EXISTS records_resource_live
                    ON records(resource, deleted_at, updated_at DESC);
                CREATE TABLE IF NOT EXISTS activity (
                    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                    action TEXT NOT NULL,
                    resource TEXT NOT NULL,
                    record_id TEXT,
                    title TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    details TEXT NOT NULL DEFAULT '{}'
                );
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS habit_checks (
                    habit_id TEXT NOT NULL REFERENCES records(id) ON DELETE CASCADE,
                    day TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    PRIMARY KEY (habit_id, day)
                );
                CREATE TABLE IF NOT EXISTS focus_sessions (
                    id TEXT PRIMARY KEY,
                    task_id TEXT REFERENCES records(id) ON DELETE SET NULL,
                    started_at TEXT NOT NULL,
                    finished_at TEXT,
                    planned_seconds INTEGER NOT NULL,
                    elapsed_seconds INTEGER NOT NULL DEFAULT 0,
                    status TEXT NOT NULL,
                    label TEXT NOT NULL DEFAULT ''
                );
                CREATE UNIQUE INDEX IF NOT EXISTS one_active_focus
                    ON focus_sessions((1)) WHERE status = 'running';
                PRAGMA user_version=1;
                COMMIT;
            """)

    @staticmethod
    def schema(resource):
        if not isinstance(resource, str) or resource not in RESOURCES:
            raise NotFound("Sezione non trovata")
        return RESOURCES[resource]

    @staticmethod
    def unpack(row):
        result = json.loads(row["payload"])
        result.update({name: row[name] for name in ("id", "resource", "created_at", "updated_at", "deleted_at", "revision")})
        return result

    @staticmethod
    def _search_text(schema, payload):
        values = []
        for key in schema["search_fields"]:
            value = payload.get(key)
            if isinstance(value, list):
                values.extend(str(item) for item in value)
            elif value is not None:
                values.append(str(value))
        return " ".join(values).casefold()

    def _row(self, db, resource, record_id, *, deleted=None):
        self.schema(resource)
        row = db.execute("SELECT * FROM records WHERE id=? AND resource=?", (record_id, resource)).fetchone()
        if row is None or (deleted is False and row["deleted_at"] is not None):
            raise NotFound("Elemento non trovato")
        return row

    @staticmethod
    def _revision(row, expected):
        if type(expected) is not int or expected < 1:
            raise WorkspaceError("La revisione è obbligatoria per modificare un elemento")
        if row["revision"] != expected:
            raise Conflict("L'elemento è cambiato in un'altra finestra. Ricaricalo prima di salvare.")

    def _references(self, db, schema, payload):
        for name, spec in schema["fields"].items():
            if spec["type"] == "reference" and payload.get(name):
                try:
                    self._row(db, spec["reference"], payload[name], deleted=False)
                except NotFound:
                    raise WorkspaceError("Il riferimento non esiste o è nel cestino", fields={name: "Seleziona un elemento disponibile"}) from None

    @staticmethod
    def _log(db, action, resource, record_id, title, details=None):
        db.execute(
            "INSERT INTO activity(action,resource,record_id,title,created_at,details) VALUES(?,?,?,?,?,?)",
            (action, resource, record_id, title, timestamp(), encode(details or {})),
        )

    def create(self, resource, payload):
        schema = self.schema(resource)
        clean = validate_record(payload, schema["fields"])
        validate_consistency(resource, clean)
        now = timestamp()
        record_id = uuid.uuid4().hex
        with self.connection(write=True) as db:
            self._references(db, schema, clean)
            db.execute(
                "INSERT INTO records(id,resource,payload,title,search_text,created_at,updated_at) VALUES(?,?,?,?,?,?,?)",
                (record_id, resource, encode(clean), clean[schema["title_field"]], self._search_text(schema, clean), now, now),
            )
            self._log(db, "created", resource, record_id, clean[schema["title_field"]])
            return self.unpack(self._row(db, resource, record_id))

    def get(self, resource, record_id):
        with self.connection() as db:
            return self.unpack(self._row(db, resource, record_id))

    def update(self, resource, record_id, payload, revision):
        schema = self.schema(resource)
        changes = validate_record(payload, schema["fields"], partial=True)
        with self.connection(write=True) as db:
            row = self._row(db, resource, record_id, deleted=False)
            self._revision(row, revision)
            clean = json.loads(row["payload"])
            clean.update(changes)
            validate_consistency(resource, clean)
            self._references(db, schema, clean)
            db.execute(
                "UPDATE records SET payload=?,title=?,search_text=?,updated_at=?,revision=revision+1 WHERE id=?",
                (encode(clean), clean[schema["title_field"]], self._search_text(schema, clean), timestamp(), record_id),
            )
            self._log(db, "updated", resource, record_id, clean[schema["title_field"]], {"fields": list(changes)})
            return self.unpack(self._row(db, resource, record_id))

    def trash(self, resource, record_id, revision):
        with self.connection(write=True) as db:
            row = self._row(db, resource, record_id, deleted=False)
            self._revision(row, revision)
            now = timestamp()
            db.execute("UPDATE records SET deleted_at=?,updated_at=?,revision=revision+1 WHERE id=?", (now, now, record_id))
            self._log(db, "trashed", resource, record_id, row["title"])
            return self.unpack(self._row(db, resource, record_id))

    def restore(self, resource, record_id, revision):
        with self.connection(write=True) as db:
            row = self._row(db, resource, record_id)
            self._revision(row, revision)
            if row["deleted_at"] is None:
                raise Conflict("L'elemento è già attivo")
            db.execute("UPDATE records SET deleted_at=NULL,updated_at=?,revision=revision+1 WHERE id=?", (timestamp(), record_id))
            self._log(db, "restored", resource, record_id, row["title"])
            return self.unpack(self._row(db, resource, record_id))

    def duplicate(self, resource, record_id):
        schema = self.schema(resource)
        original = self.get(resource, record_id)
        payload = {key: original.get(key) for key in schema["fields"]}
        title_field = schema["title_field"]
        limit = schema["fields"][title_field]["max_length"]
        payload[title_field] = payload[title_field][:limit - 8] + " (copia)"
        return self.create(resource, payload)

    def list(self, resource, *, query="", filters=None, sort="updated_at", direction="desc", page=1, page_size=50, trash=False):
        schema = self.schema(resource)
        page = positive_int(page, "Pagina")
        page_size = positive_int(page_size, "Elementi per pagina", maximum=200)
        if sort not in schema["sorts"]:
            raise WorkspaceError("Ordinamento non disponibile")
        if direction not in ("asc", "desc"):
            raise WorkspaceError("Direzione di ordinamento non valida")
        if not isinstance(query, str) or len(query) > 1000:
            raise WorkspaceError("La ricerca deve contenere al massimo 1000 caratteri")
        clauses = ["resource=?", "deleted_at IS NOT NULL" if trash else "deleted_at IS NULL"]
        args = [resource]
        if query.strip():
            clauses.append("instr(search_text, ?) > 0")
            args.append(query.strip().casefold())
        for key, value in (filters or {}).items():
            if key not in schema["filters"]:
                raise WorkspaceError(f"Filtro non disponibile: {key}")
            spec = schema["fields"][key]
            if spec["type"] == "boolean":
                if value not in (True, False, "true", "false"):
                    raise WorkspaceError("Filtro booleano non valido")
                value = int(value is True or value == "true")
            clauses.append(f"json_extract(payload, '$.{key}') = ?")
            args.append(value)
        where = " AND ".join(clauses)
        if sort in ("created_at", "updated_at"):
            order = sort
        else:
            order = f"json_extract(payload, '$.{sort}')"
        # Missing deadlines belong at the end in both directions.
        ordering = f"({order} IS NULL) ASC, {order} {direction.upper()}, id ASC"
        with self.connection() as db:
            count = db.execute(f"SELECT COUNT(*) FROM records WHERE {where}", args).fetchone()[0]
            rows = db.execute(
                f"SELECT * FROM records WHERE {where} ORDER BY {ordering} LIMIT ? OFFSET ?",
                [*args, page_size, (page - 1) * page_size],
            ).fetchall()
        return {"items": [self.unpack(row) for row in rows], "total": count, "page": page, "page_size": page_size, "pages": max(1, (count + page_size - 1) // page_size)}

    def all_live(self, db, resource=None):
        if resource:
            self.schema(resource)
            rows = db.execute("SELECT * FROM records WHERE resource=? AND deleted_at IS NULL", (resource,)).fetchall()
        else:
            rows = db.execute("SELECT * FROM records WHERE deleted_at IS NULL").fetchall()
        return [self.unpack(row) for row in rows]

    def search(self, query, *, limit=40):
        if not isinstance(query, str) or len(query) > 1000:
            raise WorkspaceError("Ricerca non valida")
        query = query.strip().casefold()
        if not query:
            return {"items": [], "total": 0}
        limit = positive_int(limit, "Limite", maximum=200)
        with self.connection() as db:
            rows = db.execute(
                "SELECT * FROM records WHERE deleted_at IS NULL AND instr(search_text, ?) > 0 ORDER BY updated_at DESC LIMIT ?",
                (query, limit),
            ).fetchall()
            total = db.execute("SELECT COUNT(*) FROM records WHERE deleted_at IS NULL AND instr(search_text, ?) > 0", (query,)).fetchone()[0]
        return {"items": [self.unpack(row) for row in rows], "total": total}

    def activity(self, *, page=1, page_size=40):
        page = positive_int(page, "Pagina")
        page_size = positive_int(page_size, "Elementi per pagina", maximum=200)
        with self.connection() as db:
            total = db.execute("SELECT COUNT(*) FROM activity").fetchone()[0]
            rows = db.execute("SELECT * FROM activity ORDER BY sequence DESC LIMIT ? OFFSET ?", (page_size, (page - 1) * page_size)).fetchall()
        items = [{**dict(row), "details": json.loads(row["details"])} for row in rows]
        return {"items": items, "total": total, "page": page, "page_size": page_size, "pages": max(1, (total + page_size - 1) // page_size)}

    def get_settings(self):
        result = {key: deepcopy(spec["default"]) for key, spec in SETTINGS.items()}
        with self.connection() as db:
            for row in db.execute("SELECT key,value FROM settings"):
                if row["key"] in SETTINGS:
                    result[row["key"]] = json.loads(row["value"])
        return result

    def save_settings(self, payload):
        clean = validate_record(payload, SETTINGS, partial=True)
        if any(value is None for value in clean.values()):
            raise WorkspaceError("Le preferenze non possono essere vuote")
        with self.connection(write=True) as db:
            for key, value in clean.items():
                db.execute("INSERT INTO settings(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, encode(value)))
            self._log(db, "settings", "settings", None, "Preferenze aggiornate", {"fields": list(clean)})
        return self.get_settings()

    def habit_check(self, habit_id, day, checked):
        from .validation import validate_field
        from .schema import field
        day = validate_field(day, field("Data", "date", required=True))
        if type(checked) is not bool:
            raise WorkspaceError("checked deve essere vero o falso")
        if day > date.today().isoformat():
            raise WorkspaceError("Puoi segnare solo oggi o un giorno passato")
        with self.connection(write=True) as db:
            row = self._row(db, "habits", habit_id, deleted=False)
            if checked:
                db.execute("INSERT OR IGNORE INTO habit_checks(habit_id,day,created_at) VALUES(?,?,?)", (habit_id, day, timestamp()))
            else:
                db.execute("DELETE FROM habit_checks WHERE habit_id=? AND day=?", (habit_id, day))
            self._log(db, "habit_checked" if checked else "habit_unchecked", "habits", habit_id, row["title"], {"day": day})
        return {"habit_id": habit_id, "day": day, "checked": checked}

    def habit_history(self, days=35):
        days = positive_int(days, "Giorni", maximum=366)
        since = (date.today() - timedelta(days=days - 1)).isoformat()
        with self.connection() as db:
            rows = db.execute(
                "SELECT h.habit_id,h.day FROM habit_checks h JOIN records r ON r.id=h.habit_id WHERE h.day>=? AND r.deleted_at IS NULL ORDER BY h.day",
                (since,),
            ).fetchall()
        return {"since": since, "days": days, "checks": [dict(row) for row in rows]}

    def start_focus(self, minutes, *, task_id=None, label=""):
        minutes = positive_int(minutes, "Minuti", maximum=180)
        if not isinstance(label, str) or len(label) > 240:
            raise WorkspaceError("Titolo della sessione non valido")
        with self.connection(write=True) as db:
            if db.execute("SELECT 1 FROM focus_sessions WHERE status='running'").fetchone():
                raise Conflict("Una sessione è già in corso")
            if task_id:
                self._row(db, "tasks", task_id, deleted=False)
            session_id = uuid.uuid4().hex
            db.execute(
                "INSERT INTO focus_sessions(id,task_id,started_at,planned_seconds,status,label) VALUES(?,?,?,?,?,?)",
                (session_id, task_id, timestamp(), minutes * 60, "running", label.strip()),
            )
            self._log(db, "focus_started", "focus", session_id, label or "Sessione di concentrazione")
            return dict(db.execute("SELECT * FROM focus_sessions WHERE id=?", (session_id,)).fetchone())

    def finish_focus(self, session_id, *, cancel=False):
        with self.connection(write=True) as db:
            row = db.execute("SELECT * FROM focus_sessions WHERE id=?", (session_id,)).fetchone()
            if row is None:
                raise NotFound("Sessione non trovata")
            if row["status"] != "running":
                raise Conflict("La sessione è già terminata")
            now = datetime.now(timezone.utc)
            elapsed = max(0, int((now - datetime.fromisoformat(row["started_at"])).total_seconds()))
            elapsed = min(elapsed, row["planned_seconds"])
            status = "cancelled" if cancel else "completed" if elapsed >= row["planned_seconds"] else "stopped"
            db.execute("UPDATE focus_sessions SET finished_at=?,elapsed_seconds=?,status=? WHERE id=?", (now.isoformat(), elapsed, status, session_id))
            self._log(db, "focus_finished", "focus", session_id, row["label"] or "Sessione di concentrazione", {"seconds": elapsed, "status": status})
            return dict(db.execute("SELECT * FROM focus_sessions WHERE id=?", (session_id,)).fetchone())

    def focus_status(self):
        with self.connection() as db:
            running = db.execute("SELECT * FROM focus_sessions WHERE status='running'").fetchone()
            recent = db.execute("SELECT * FROM focus_sessions ORDER BY started_at DESC LIMIT 30").fetchall()
        return {"running": dict(running) if running else None, "recent": [dict(row) for row in recent]}

    def summary(self):
        today = date.today()
        today_text = today.isoformat()
        week_start = today - timedelta(days=today.weekday())
        month = today_text[:7]
        with self.connection() as db:
            records = self.all_live(db)
            trash_count = db.execute("SELECT COUNT(*) FROM records WHERE deleted_at IS NOT NULL").fetchone()[0]
            sessions = [dict(row) for row in db.execute("SELECT * FROM focus_sessions WHERE status IN ('completed','stopped') ORDER BY started_at DESC LIMIT 1000")]
        groups = {resource: [] for resource in RESOURCES}
        for record in records:
            groups[record["resource"]].append(record)
        tasks = groups["tasks"]
        open_tasks = [task for task in tasks if task["status"] != "done"]
        overdue = [task for task in open_tasks if task.get("due_date") and task["due_date"] < today_text]
        today_tasks = [task for task in open_tasks if task.get("due_date") == today_text]
        upcoming = sorted((event for event in groups["events"] if event["end_at"] >= today_text), key=lambda item: item["start_at"])[:8]
        monthly = [item for item in groups["expenses"] if item["date"].startswith(month)]
        income = sum(item["amount_cents"] for item in monthly if item["direction"] == "income")
        expenses = sum(item["amount_cents"] for item in monthly if item["direction"] == "expense")
        categories = {}
        for item in monthly:
            if item["direction"] == "expense":
                categories[item["category"]] = categories.get(item["category"], 0) + item["amount_cents"]
        focus_today = []
        for session in sessions:
            local_day = datetime.fromisoformat(session["started_at"]).astimezone().date()
            if local_day == today:
                focus_today.append(session)
        project_progress = []
        for project in groups["projects"]:
            related = [task for task in tasks if task.get("project_id") == project["id"]]
            done = sum(task["status"] == "done" for task in related)
            project_progress.append({**project, "task_count": len(related), "done_count": done, "progress": round(done / len(related) * 100) if related else 0})
        return {
            "today": today_text,
            "week_start": week_start.isoformat(),
            "counts": {key: len(value) for key, value in groups.items()},
            "tasks": {"open": len(open_tasks), "done": len(tasks) - len(open_tasks), "overdue": len(overdue), "today": len(today_tasks), "items": sorted(overdue + today_tasks, key=lambda task: task["due_date"])[:10]},
            "projects": sorted(project_progress, key=lambda item: (not item.get("pinned"), item["updated_at"]), reverse=False),
            "events": upcoming,
            "pinned": sorted((record for record in records if record.get("pinned")), key=lambda item: item["updated_at"], reverse=True)[:12],
            "recent": sorted(records, key=lambda item: item["updated_at"], reverse=True)[:8],
            "money": {"month": month, "income_cents": income, "expense_cents": expenses, "balance_cents": income - expenses, "categories": categories},
            "focus": {"seconds_today": sum(item["elapsed_seconds"] for item in focus_today), "sessions_today": sum(item["status"] == "completed" for item in focus_today)},
            "trash_count": trash_count,
        }

    def trash_list(self):
        with self.connection() as db:
            rows = db.execute("SELECT * FROM records WHERE deleted_at IS NOT NULL ORDER BY deleted_at DESC LIMIT 200").fetchall()
            count = db.execute("SELECT COUNT(*) FROM records WHERE deleted_at IS NOT NULL").fetchone()[0]
        return {"items": [self.unpack(row) for row in rows], "total": count}

    def export_bundle(self):
        # One read transaction gives records, checks, settings and sessions a
        # consistent snapshot, even when other tabs are making changes.
        with self.connection() as db:
            db.execute("BEGIN")
            records = [self.unpack(row) for row in db.execute("SELECT * FROM records ORDER BY resource,created_at,id")]
            settings = {row["key"]: json.loads(row["value"]) for row in db.execute("SELECT * FROM settings")}
            checks = [dict(row) for row in db.execute("SELECT * FROM habit_checks ORDER BY habit_id,day")]
            sessions = [dict(row) for row in db.execute("SELECT * FROM focus_sessions ORDER BY started_at")]
        return {"format": "franco-workspace", "version": self.EXPORT_VERSION, "exported_at": timestamp(), "records": records, "settings": settings, "habit_checks": checks, "focus_sessions": sessions}

    def import_bundle(self, bundle):
        """Merge a validated export atomically; conflicting IDs are never replaced.

        Running timers are imported as cancelled because elapsed wall-clock time
        cannot safely be resumed on another machine. Existing IDs abort the
        import rather than silently overwriting newer local edits.
        """
        if not isinstance(bundle, dict) or bundle.get("format") != "franco-workspace" or bundle.get("version") != self.EXPORT_VERSION:
            raise WorkspaceError("Formato di backup non supportato")
        records = bundle.get("records")
        if not isinstance(records, list) or len(records) > self.MAX_IMPORT_RECORDS:
            raise WorkspaceError(f"Il backup deve contenere al massimo {self.MAX_IMPORT_RECORDS} elementi")
        settings = validate_record(bundle.get("settings", {}), SETTINGS, partial=True)
        if any(value is None for value in settings.values()):
            raise WorkspaceError("Preferenze non valide nel backup")
        checks = bundle.get("habit_checks", [])
        sessions = bundle.get("focus_sessions", [])
        if not isinstance(checks, list) or len(checks) > 100000 or not isinstance(sessions, list) or len(sessions) > 100000:
            raise WorkspaceError("Il backup contiene troppe sessioni o registrazioni")
        clean_records = []
        ids = set()
        import re
        for record in records:
            if not isinstance(record, dict):
                raise WorkspaceError("Elemento non valido nel backup")
            resource = record.get("resource")
            schema = self.schema(resource)
            record_id = record.get("id")
            if not isinstance(record_id, str) or not re.fullmatch(r"[0-9a-f]{32}", record_id) or record_id in ids:
                raise WorkspaceError("Identificativo duplicato o non valido nel backup")
            ids.add(record_id)
            payload = validate_record({key: record[key] for key in schema["fields"] if key in record}, schema["fields"])
            validate_consistency(resource, payload)
            dates = {}
            for key in ("created_at", "updated_at", "deleted_at"):
                value = record.get(key)
                if key == "deleted_at" and value is None:
                    dates[key] = None
                    continue
                try:
                    parsed = datetime.fromisoformat(value)
                    if parsed.tzinfo is None:
                        raise ValueError()
                    dates[key] = parsed.astimezone(timezone.utc).isoformat()
                except (TypeError, ValueError):
                    raise WorkspaceError("Data non valida nel backup") from None
            clean_records.append((record_id, resource, payload, dates))
        with self.connection(write=True) as db:
            for record_id, resource, payload, dates in clean_records:
                if db.execute("SELECT 1 FROM records WHERE id=?", (record_id,)).fetchone():
                    raise Conflict("Il backup contiene elementi già presenti. Importazione annullata senza modifiche.")
                schema = self.schema(resource)
                db.execute(
                    "INSERT INTO records(id,resource,payload,title,search_text,created_at,updated_at,deleted_at) VALUES(?,?,?,?,?,?,?,?)",
                    (record_id, resource, encode(payload), payload[schema["title_field"]], self._search_text(schema, payload), dates["created_at"], dates["updated_at"], dates["deleted_at"]),
                )
            # References may target another imported record, including a project
            # in the trash. They must still point to the expected resource.
            for _, resource, payload, _ in clean_records:
                for key, spec in self.schema(resource)["fields"].items():
                    if spec["type"] == "reference" and payload.get(key):
                        self._row(db, spec["reference"], payload[key])
            for check in checks:
                if not isinstance(check, dict):
                    raise WorkspaceError("Registrazione abitudine non valida")
                self._row(db, "habits", check.get("habit_id"))
                try:
                    day = date.fromisoformat(check.get("day"))
                except (TypeError, ValueError):
                    raise WorkspaceError("Data abitudine non valida") from None
                db.execute("INSERT OR IGNORE INTO habit_checks(habit_id,day,created_at) VALUES(?,?,?)", (check["habit_id"], day.isoformat(), timestamp()))
            for session in sessions:
                if not isinstance(session, dict):
                    raise WorkspaceError("Sessione non valida")
                session_id = session.get("id")
                if not isinstance(session_id, str) or not re.fullmatch(r"[0-9a-f]{32}", session_id):
                    raise WorkspaceError("Identificativo sessione non valido")
                planned = positive_int(session.get("planned_seconds"), "Durata", maximum=10800)
                elapsed = session.get("elapsed_seconds", 0)
                if type(elapsed) is not int or not 0 <= elapsed <= planned:
                    raise WorkspaceError("Durata trascorsa non valida")
                status = session.get("status")
                if status not in ("running", "completed", "stopped", "cancelled"):
                    raise WorkspaceError("Stato sessione non valido")
                task_id = session.get("task_id")
                if task_id:
                    self._row(db, "tasks", task_id)
                try:
                    started = datetime.fromisoformat(session.get("started_at"))
                    if started.tzinfo is None:
                        raise ValueError()
                    finished = datetime.fromisoformat(session["finished_at"]) if session.get("finished_at") else None
                    if finished and (finished.tzinfo is None or finished < started):
                        raise ValueError()
                except (TypeError, ValueError):
                    raise WorkspaceError("Orario sessione non valido") from None
                label = session.get("label", "")
                if not isinstance(label, str) or len(label) > 240:
                    raise WorkspaceError("Titolo sessione non valido")
                if status == "running":
                    status = "cancelled"
                    finished = started
                    elapsed = 0
                if status != "running" and finished is None:
                    raise WorkspaceError("Manca l'orario di fine sessione")
                try:
                    db.execute(
                        "INSERT INTO focus_sessions(id,task_id,started_at,finished_at,planned_seconds,elapsed_seconds,status,label) VALUES(?,?,?,?,?,?,?,?)",
                        (session_id, task_id, started.isoformat(), finished.isoformat(), planned, elapsed, status, label),
                    )
                except sqlite3.IntegrityError:
                    raise Conflict("Una sessione del backup è già presente") from None
            for key, value in settings.items():
                # Keep existing preferences; restore missing ones from backup.
                db.execute("INSERT OR IGNORE INTO settings(key,value) VALUES(?,?)", (key, encode(value)))
            self._log(db, "imported", "workspace", None, "Backup importato", {"records": len(clean_records)})
        return {"imported": len(clean_records), "habit_checks": len(checks), "focus_sessions": len(sessions)}

    def integrity(self):
        with self.connection() as db:
            result = db.execute("PRAGMA quick_check").fetchone()[0]
            count = db.execute("SELECT COUNT(*) FROM records").fetchone()[0]
        return {"ok": result == "ok", "records": count, "database_bytes": self.path.stat().st_size, "schema_version": self.SCHEMA_VERSION}
