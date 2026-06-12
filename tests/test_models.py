import pytest
from models.user import User
from models.person import Person

def test_user_inheritance():
    """Test that User inherits from Person and implements abstract method."""
    user = User("Rick", "rick@test.com", 1)
    assert isinstance(user, Person)
    assert user.get_role() == "Team Member"
    assert str(user) == "Rick - Team Member"

def test_person_cannot_instantiate():
    """Test that Person ABC cannot be instantiated directly."""
    with pytest.raises(TypeError):
        Person("Test", "test@test.com")

from models.project import Project
from models.task import Task, TaskStatus

def test_project_adds_member():
    """Test Project composition with User objects."""
    user = User("Rick", "r@r.com", 1)
    project = Project(1, "CLI App", "test")
    project.add_member(user)
    assert len(project.members) == 1
    assert project.members[0].get_role() == "Team Member"

def test_task_status_flow():
    """Test Task enum and state transitions."""
    task = Task(1, "Write code", 1)
    assert task.status == TaskStatus.TODO
    task.assign_to(99)
    assert task.status == TaskStatus.DOING
    assert task.assigned_to == 99
    task.complete()
    assert task.status == TaskStatus.DONE