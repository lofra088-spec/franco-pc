"""Portable data exports with spreadsheet-safe CSV cells."""
import csv
import io
import json
import re

from .schema import RESOURCES


def csv_cell(value):
    if value is None:
        return ""
    if isinstance(value, list):
        value = ", ".join(str(item) for item in value)
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        value = str(value)
    # Avoid formula execution when a downloaded CSV is opened in Excel.
    if value.lstrip().startswith(("=", "+", "-", "@")) or value.startswith(("\t", "\r", "\n")):
        value = "'" + value
    return value


def records_csv(resource, items):
    fields = ["id", *RESOURCES[resource]["fields"], "created_at", "updated_at"]
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(fields)
    for item in items:
        writer.writerow([csv_cell(item.get(key)) for key in fields])
    return ("\ufeff" + stream.getvalue()).encode("utf-8")


def safe_filename(title, extension):
    title = re.sub(r"[^\w .-]", "_", title, flags=re.UNICODE).strip(" .")[:80]
    return (title or "franco-export") + "." + extension


def note_markdown(record):
    parts = ["# " + record["title"], "", record.get("content", "")]
    if record.get("tags"):
        parts.extend(["", "Tag: " + ", ".join(record["tags"])])
    return ("\n".join(parts) + "\n").encode("utf-8")


def json_bytes(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False).encode("utf-8")
