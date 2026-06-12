from enum import Enum

class TaskStatus(Enum):
    TODO = "todo"
    DOING = "doing" 
    DONE = "done"

class Task:
    """Represents a task assigned to a User within a Project."""
    
    def __init__(self, task_id: int, title: str, project_id: int):
        self.task_id = task_id
        self.title = title
        self.project_id = project_id
        self.status = TaskStatus.TODO
        self.assigned_to: int | None = None
    
    def assign_to(self, user_id: int) -> None:
        """Assign task to a user ID."""
        self.assigned_to = user_id
        self.status = TaskStatus.DOING
    
    def complete(self) -> None:
        """Mark task as done."""
        self.status = TaskStatus.DONE
    
    def __str__(self) -> str:
        return f"Task {self.task_id}: {self.title} [{self.status.value}]"