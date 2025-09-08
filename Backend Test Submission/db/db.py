import json
import os
from threading import Lock

DB_FILE = "db.json"
_lock = Lock()

# Load database from file (or create new one)
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        try:
            database = json.load(f)
        except json.JSONDecodeError:
            database = {}
else:
    database = {}

def save_db():
    """Persist current database dictionary to JSON file."""
    with _lock:
        with open(DB_FILE, "w") as f:
            json.dump(database, f, indent=4, default=str)  # datetime will be str
