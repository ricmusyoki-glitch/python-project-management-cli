from abc import ABC, abstractmethod

class Person(ABC):
    """Base class for all people in the system. Demonstrates inheritance + abstraction."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    @abstractmethod
    def get_role(self) -> str:
        """Return the role of this person. Must be implemented by subclasses."""
        pass
    
    def __str__(self) -> str:
        return f"{self.name} - {self.get_role()}"