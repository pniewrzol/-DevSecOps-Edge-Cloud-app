"""Offline-first demonstrator. Only fictional plates; no physical barrier actuator."""
from datetime import date, datetime, timezone
from pathlib import Path
import os
import re
import sqlite3

PLATE_PATTERN = re.compile(r"^[A-Z0-9]{4,12}$")


def db_path() -> Path:
    return Path(os.environ.get("SMARTGATE_DB_PATH", ".local/smartgate.db"))


def connection():
    path = db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, timeout=5)
    conn.row_factory = sqlite3.Row
    return conn


def initialize() -> None:
    """Demo seed is idempotent; license plates are intentionally fictional."""
    with connection() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS permits (
            plate TEXT PRIMARY KEY, valid_until TEXT NOT NULL, active INTEGER NOT NULL)""")
        db.execute("""CREATE TABLE IF NOT EXISTS access_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT, plate TEXT NOT NULL,
            decision TEXT NOT NULL, reason TEXT NOT NULL,
            occurred_at TEXT NOT NULL, synced INTEGER NOT NULL DEFAULT 0)""")
        db.executemany("INSERT OR IGNORE INTO permits VALUES (?, ?, ?)", [
            ("SK12345", "2099-12-31", 1),
            ("KR98765", "2099-12-31", 0),
            ("SB2026A", "2020-01-01", 1),
        ])


def check_plate(plate: str):
    normalized = re.sub(r"[ -]", "", plate.strip().upper())
    if not PLATE_PATTERN.fullmatch(normalized):
        raise ValueError("Invalid fictional plate format: 4–12 alphanumeric characters")
    with connection() as db:
        row = db.execute("SELECT active, valid_until FROM permits WHERE plate = ?", (normalized,)).fetchone()
        if row is None:
            decision, reason = "DENY", "not_registered"
        elif not row["active"]:
            decision, reason = "DENY", "inactive"
        elif row["valid_until"] < date.today().isoformat():
            decision, reason = "DENY", "expired"
        else:
            decision, reason = "OPEN", "active_permit"
        db.execute("INSERT INTO access_events (plate,decision,reason,occurred_at) VALUES (?,?,?,?)",
                   (normalized, decision, reason, datetime.now(timezone.utc).isoformat()))
    return {"plate": normalized, "decision": decision, "reason": reason, "simulated": True}


def event_summary():
    """Only aggregate events are exposed: no plate data in the report."""
    with connection() as db:
        rows = db.execute("SELECT decision, count(*) AS total FROM access_events GROUP BY decision").fetchall()
        queued = db.execute("SELECT count(*) FROM access_events WHERE synced = 0").fetchone()[0]
    return {"counts": {row["decision"]: row["total"] for row in rows},
            "pending_sync": queued, "cloud_sync_implemented": False}
