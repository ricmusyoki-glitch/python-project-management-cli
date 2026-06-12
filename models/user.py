from .person import Person

class User(Person):
    """User inherits from Person. Represents a project team member."""
    
    def __init__(self, name: str, email: str, user_id: int):
        super().__init__(name, email)
        self.user_id = user_id
    
    def get_role(self) -> str:
        return "Team Member"