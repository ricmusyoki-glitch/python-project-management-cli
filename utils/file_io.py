import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path("data/storage.json")

def load_data() -> Dict:
    """Load all data from JSON. Creates file if missing. Handles corrupt JSON."""
    try:
        if not DATA_FILE.exists():
            DATA_FILE.parent.mkdir(exist_ok=True)
            return {"users": [], "projects": [], "tasks": []}
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"users": [], "projects": [], "tasks": []}
    except Exception as e:
        raise IOError(f"Failed to load data: {e}")

def save_data(data: Dict) -> None:
    """Save data to JSON file with pretty formatting."""
    try:
        DATA_FILE.parent.mkdir(exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        raise IOError(f"Failed to save data: {e}")