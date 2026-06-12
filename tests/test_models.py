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