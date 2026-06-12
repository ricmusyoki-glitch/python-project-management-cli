import typer
from rich.console import Console
from models.user import User
from utils.file_io import load_data, save_data
from models.project import Project
from models.task import Task, TaskStatus

console = Console()
app = typer.Typer(help="Project Management CLI")

@app.command()
def add_user(name: str, email: str):
    """Add a new user."""
    data = load_data()
    new_id = len(data["users"]) + 1
    user = User(name, email, new_id)
    data["users"].append({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.get_role()
    })
    save_data(data)
    console.print(f"[green]✓ Added user:[/green] {user}")

@app.command()
def list_users():
    """List all users."""
    data = load_data()
    if not data["users"]:
        console.print("[yellow]No users found.[/yellow]")
        return
    for u in data["users"]:
        console.print(f"ID {u['id']}:[/cyan] {u['name']} - {u['email']}")

@app.command()
def add_project(name: str, description: str):
    """Add a new project."""
    data = load_data()
    new_id = len(data["projects"]) + 1
    project = Project(new_id, name, description)
    data["projects"].append({
        "id": project.project_id,
        "name": project.name,
        "description": project.description,
        "members": []
    })
    save_data(data)
    console.print(f"[green]✓ Added project:[/green] {name} with ID {new_id}")

@app.command()
def list_projects():
    """List all projects."""
    data = load_data()
    if not data["projects"]:
        console.print("[yellow]No projects found.[/yellow]")
        return
    for p in data["projects"]:
        console.print(f"[cyan]ID {p['id']}:[/cyan] {p['name']} - {p['description']}")

@app.command()
def add_task(title: str, project_id: int):
    """Add a task to a project."""
    data = load_data()
    if not any(p["id"] == project_id for p in data["projects"]):
        console.print(f"[red]Error: Project {project_id} not found.[/red]")
        return

    new_id = len(data["tasks"]) + 1
    task = Task(new_id, title, project_id)
    data["tasks"].append({
        "id": task.task_id,
        "title": task.title,
        "project_id": task.project_id,
        "status": task.status.value,
        "assigned_to": task.assigned_to
    })
    save_data(data)
    console.print(f"[green]✓ Added task:[/green] {title} to project {project_id}")

if __name__ == "__main__":
    app()