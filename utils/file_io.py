import json
from pathlib import Path
from rich.console import Console

console = Console()
DATA_FILE = Path("data/storage.json")

def load_data():
    """Load all data. Returns dict with users, projects, tasks keys."""
    try:
        if not DATA_FILE.exists():
            return {"users": [], "projects": [], "tasks": []}
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            # Backwards compat for old files
            if "projects" not in data:
                data["projects"] = []
            if "tasks" not in data:
                data["tasks"] = []
            return data
    except json.JSONDecodeError:
        console.print("[bold red]Error: storage.json is corrupted.[/bold red]")
        return {"users": [], "projects": [], "tasks": []}
    except Exception as e:
        console.print(f"[bold red]Error loading data: {e}[/bold red]")
        return {"users": [], "projects": [], "tasks": []}

def save_data(data: dict):
    """Save all data to JSON file."""
    try:
        DATA_FILE.parent.mkdir(exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        console.print(f"[bold red]Error saving data: {e}[/bold red]")