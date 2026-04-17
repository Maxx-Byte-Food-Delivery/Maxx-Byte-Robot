import pytest
from django.contrib.auth.models import User

@pytest.fixture
#makes user
def user(db):
  user = User.objects.create_user(username="john doe", password ="psswrd123")
  user.save()
  return user
#makes multiple users
def users(db):
  user1 = User(username="john doe", password ="psswrd123")
  user2 = User(username="jane doe", password ="SomeG00dPasswor!d")
  user3 = User(username="SomeUser", password="G00dPassw0rd!")
  user1.save()
  user2.save()
  user3.save()
  return users