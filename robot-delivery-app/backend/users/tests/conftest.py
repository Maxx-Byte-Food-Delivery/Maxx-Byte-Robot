import pytest
from users.models import User

@pytest.fixture
def user():
  return User(username="john doe", password="psswrd123")

def test_user_initialization(sample_user):
  assert sample_user.username = "john doe"
  assert sample_user.password != ("psswrd123")