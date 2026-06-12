import typer
from rich import print
from models.user import User
from utils.file_io import load_data, save_data

app = typer.Typer(help="Project Management CLI")

@app.command()
def add_user(name: str, email: str):
    """Add a new user to the system."""
    data = load_data()
    user_id = len(data["users"]) + 1
    user = User(name, email, user_id)
    data["users"].append({"id": user_id, "name": name, "email": email})
    save_data(data)
    print(f"[green]✓ Added user:[/green] {user}")

@app.command()
def list_users():
    """List all users in the system."""
    data = load_data()
    if not data["users"]:
        print("[yellow]No users found.[/yellow]")
        return
    for u in data["users"]:
        print(f"[cyan]{u['id']}:[/cyan] {u['name']} - {u['email']}")

if __name__ == "__main__":
    app()