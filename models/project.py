from.person import Person

class Project:
    """Represents a project. Uses composition - has a list of Users."""
    
    def __init__(self, project_id: int, name: str, description: str):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.members: list[Person] = []
    
    def add_member(self, user: Person) -> None:
        """Add a Person to this project. Demonstrates polymorphism."""
        self.members.append(user)
    
    def __str__(self) -> str:
        return f"Project {self.project_id}: {self.name} - {len(self.members)} members"