"""One schema for storage validation, forms, filters, and exports.

Resource names and field names are developer-controlled identifiers. User data
never contributes SQL identifiers. Dates use ISO representations; money uses
integer cents to avoid rounding errors.
"""
from copy import deepcopy


def field(label, kind="text", *, required=False, default=None, options=None,
          max_length=240, minimum=None, maximum=None, reference=None, help=""):
    result = {
        "label": label,
        "type": kind,
        "required": required,
        "default": default,
        "max_length": max_length,
        "help": help,
    }
    if options is not None:
        result["options"] = options
    if minimum is not None:
        result["minimum"] = minimum
    if maximum is not None:
        result["maximum"] = maximum
    if reference:
        result["reference"] = reference
    return result


COLORS = ["indigo", "violet", "blue", "cyan", "emerald", "amber", "rose", "slate"]
PRIORITIES = ["low", "normal", "high", "urgent"]
RESOURCES = {
    "projects": {
        "label": "Progetti",
        "singular": "progetto",
        "icon": "layers",
        "description": "Dall'idea al risultato, con un posto per ogni attività.",
        "title_field": "title",
        "fields": {
            "title": field("Nome progetto", required=True, max_length=180),
            "description": field("Descrizione", "multiline", default="", max_length=20000),
            "status": field("Stato", "select", default="active", options=["planned", "active", "paused", "completed"]),
            "color": field("Colore", "select", default="indigo", options=COLORS),
            "due_date": field("Scadenza", "date"),
            "tags": field("Tag", "tags", default=[]),
            "pinned": field("In evidenza", "boolean", default=False),
        },
        "search_fields": ["title", "description", "tags"],
        "filters": ["status", "color", "pinned"],
        "sorts": ["updated_at", "created_at", "title", "due_date"],
    },
    "tasks": {
        "label": "Attività",
        "singular": "attività",
        "icon": "check-square",
        "description": "Una lista chiara, una cosa alla volta.",
        "title_field": "title",
        "fields": {
            "title": field("Cosa vuoi fare?", required=True, max_length=240),
            "description": field("Dettagli", "multiline", default="", max_length=20000),
            "status": field("Stato", "select", default="todo", options=["todo", "doing", "done"]),
            "priority": field("Priorità", "select", default="normal", options=PRIORITIES),
            "project_id": field("Progetto", "reference", reference="projects"),
            "due_date": field("Scadenza", "date"),
            "estimate_minutes": field("Minuti stimati", "integer", default=0, minimum=0, maximum=100000),
            "tags": field("Tag", "tags", default=[]),
            "pinned": field("In evidenza", "boolean", default=False),
        },
        "search_fields": ["title", "description", "tags"],
        "filters": ["status", "priority", "project_id", "pinned"],
        "sorts": ["updated_at", "created_at", "title", "due_date", "priority"],
    },
    "notes": {
        "label": "Note",
        "singular": "nota",
        "icon": "file-text",
        "description": "Cattura un pensiero. Ritrovalo quando ti serve.",
        "title_field": "title",
        "fields": {
            "title": field("Titolo", required=True, max_length=240),
            "content": field("Contenuto", "multiline", default="", max_length=100000),
            "project_id": field("Progetto", "reference", reference="projects"),
            "color": field("Colore", "select", default="slate", options=COLORS),
            "tags": field("Tag", "tags", default=[]),
            "pinned": field("In evidenza", "boolean", default=False),
        },
        "search_fields": ["title", "content", "tags"],
        "filters": ["project_id", "color", "pinned"],
        "sorts": ["updated_at", "created_at", "title"],
    },
    "bookmarks": {
        "label": "Segnalibri",
        "singular": "segnalibro",
        "icon": "bookmark",
        "description": "Le risorse utili, senza perdere il filo.",
        "title_field": "title",
        "fields": {
            "title": field("Titolo", required=True),
            "url": field("Indirizzo web", "url", required=True, max_length=4096, help="Sono ammessi solo indirizzi http e https."),
            "description": field("Descrizione", "multiline", default="", max_length=10000),
            "collection": field("Raccolta", default="Generale", max_length=100),
            "tags": field("Tag", "tags", default=[]),
            "pinned": field("In evidenza", "boolean", default=False),
        },
        "search_fields": ["title", "url", "description", "collection", "tags"],
        "filters": ["collection", "pinned"],
        "sorts": ["updated_at", "created_at", "title"],
    },
    "contacts": {
        "label": "Contatti",
        "singular": "contatto",
        "icon": "users",
        "description": "Persone, riferimenti e appunti sempre a portata di mano.",
        "title_field": "name",
        "fields": {
            "name": field("Nome", required=True, max_length=180),
            "email": field("Email", "email", default="", max_length=254),
            "phone": field("Telefono", default="", max_length=60),
            "company": field("Organizzazione", default="", max_length=180),
            "role": field("Ruolo", default="", max_length=180),
            "notes": field("Appunti", "multiline", default="", max_length=20000),
            "tags": field("Tag", "tags", default=[]),
            "pinned": field("In evidenza", "boolean", default=False),
        },
        "search_fields": ["name", "email", "phone", "company", "role", "notes", "tags"],
        "filters": ["company", "pinned"],
        "sorts": ["updated_at", "created_at", "name", "company"],
    },
    "events": {
        "label": "Agenda",
        "singular": "evento",
        "icon": "calendar",
        "description": "Dai spazio a ciò che conta, giorno per giorno.",
        "title_field": "title",
        "fields": {
            "title": field("Titolo evento", required=True),
            "start_at": field("Inizio", "datetime", required=True),
            "end_at": field("Fine", "datetime", required=True),
            "all_day": field("Tutto il giorno", "boolean", default=False),
            "location": field("Luogo o collegamento", default="", max_length=1000),
            "description": field("Descrizione", "multiline", default="", max_length=20000),
            "project_id": field("Progetto", "reference", reference="projects"),
            "color": field("Colore", "select", default="blue", options=COLORS),
            "tags": field("Tag", "tags", default=[]),
        },
        "search_fields": ["title", "location", "description", "tags"],
        "filters": ["project_id", "color", "all_day"],
        "sorts": ["updated_at", "created_at", "title", "start_at"],
    },
    "habits": {
        "label": "Abitudini",
        "singular": "abitudine",
        "icon": "repeat",
        "description": "Piccoli gesti ripetuti, progressi che si vedono.",
        "title_field": "title",
        "fields": {
            "title": field("Nome abitudine", required=True, max_length=180),
            "description": field("Perché è importante", "multiline", default="", max_length=10000),
            "target_per_week": field("Obiettivo settimanale", "integer", default=5, minimum=1, maximum=7),
            "color": field("Colore", "select", default="emerald", options=COLORS),
            "active": field("Attiva", "boolean", default=True),
            "tags": field("Tag", "tags", default=[]),
        },
        "search_fields": ["title", "description", "tags"],
        "filters": ["active", "color"],
        "sorts": ["updated_at", "created_at", "title"],
    },
    "snippets": {
        "label": "Snippet e prompt",
        "singular": "snippet",
        "icon": "code",
        "description": "Testi, comandi e prompt pronti da riutilizzare.",
        "title_field": "title",
        "fields": {
            "title": field("Titolo", required=True),
            "content": field("Testo o codice", "code", required=True, max_length=100000),
            "language": field("Tipo", "select", default="text", options=["text", "prompt", "python", "javascript", "typescript", "html", "css", "sql", "powershell", "bash", "json", "markdown"]),
            "description": field("Descrizione", "multiline", default="", max_length=10000),
            "tags": field("Tag", "tags", default=[]),
            "pinned": field("In evidenza", "boolean", default=False),
        },
        "search_fields": ["title", "content", "description", "tags"],
        "filters": ["language", "pinned"],
        "sorts": ["updated_at", "created_at", "title", "language"],
    },
    "expenses": {
        "label": "Spese",
        "singular": "movimento",
        "icon": "wallet",
        "description": "Un registro personale di entrate e uscite in euro.",
        "title_field": "title",
        "fields": {
            "title": field("Descrizione", required=True),
            "amount_cents": field("Importo in euro", "money", required=True, minimum=1, maximum=100000000000),
            "direction": field("Tipo", "select", default="expense", options=["expense", "income"]),
            "category": field("Categoria", "select", default="other", options=["food", "transport", "home", "health", "education", "leisure", "work", "subscriptions", "salary", "other"]),
            "date": field("Data", "date", required=True),
            "notes": field("Appunti", "multiline", default="", max_length=10000),
            "project_id": field("Progetto", "reference", reference="projects"),
            "tags": field("Tag", "tags", default=[]),
        },
        "search_fields": ["title", "notes", "tags"],
        "filters": ["direction", "category", "project_id"],
        "sorts": ["updated_at", "created_at", "title", "date", "amount_cents"],
    },
    "journal": {
        "label": "Diario",
        "singular": "pagina di diario",
        "icon": "book-open",
        "description": "Uno spazio per riflettere e riconoscere i progressi.",
        "title_field": "title",
        "fields": {
            "title": field("Titolo", required=True),
            "date": field("Data", "date", required=True),
            "content": field("Come è andata?", "multiline", default="", max_length=100000),
            "mood": field("Umore", "select", default="neutral", options=["great", "good", "neutral", "low", "difficult"]),
            "gratitude": field("Una cosa da ricordare", "multiline", default="", max_length=10000),
            "tags": field("Tag", "tags", default=[]),
            "pinned": field("In evidenza", "boolean", default=False),
        },
        "search_fields": ["title", "content", "gratitude", "tags"],
        "filters": ["mood", "pinned"],
        "sorts": ["updated_at", "created_at", "title", "date"],
    },
    "goals": {
        "label": "Obiettivi",
        "singular": "obiettivo",
        "icon": "target",
        "description": "Scegli una direzione e misura i passi avanti.",
        "title_field": "title",
        "fields": {
            "title": field("Obiettivo", required=True),
            "description": field("Motivazione e piano", "multiline", default="", max_length=20000),
            "target": field("Valore da raggiungere", "integer", default=100, minimum=1, maximum=1000000000),
            "current": field("Valore attuale", "integer", default=0, minimum=0, maximum=1000000000),
            "unit": field("Unità di misura", default="%", max_length=40),
            "due_date": field("Scadenza", "date"),
            "status": field("Stato", "select", default="active", options=["active", "paused", "completed"]),
            "project_id": field("Progetto", "reference", reference="projects"),
            "color": field("Colore", "select", default="violet", options=COLORS),
            "tags": field("Tag", "tags", default=[]),
        },
        "search_fields": ["title", "description", "unit", "tags"],
        "filters": ["status", "project_id", "color"],
        "sorts": ["updated_at", "created_at", "title", "due_date"],
    },
}

SETTINGS = {
    "display_name": field("Come ti chiami?", default="Franco", max_length=60),
    "theme": field("Aspetto", "select", default="dark", options=["dark", "light", "system"]),
    "accent": field("Colore principale", "select", default="indigo", options=COLORS),
    "week_start": field("Inizio settimana", "select", default="monday", options=["monday", "sunday"]),
    "compact": field("Visualizzazione compatta", "boolean", default=False),
    "reduce_motion": field("Riduci animazioni", "boolean", default=False),
    "focus_minutes": field("Minuti di concentrazione", "integer", default=25, minimum=1, maximum=180),
    "break_minutes": field("Minuti di pausa", "integer", default=5, minimum=1, maximum=60),
    "daily_focus_target": field("Sessioni al giorno", "integer", default=4, minimum=1, maximum=30),
    "home_message": field("Il tuo promemoria personale", default="Fai spazio alle cose importanti.", max_length=240),
}


def public_schema():
    return deepcopy({"resources": RESOURCES, "settings": SETTINGS})
