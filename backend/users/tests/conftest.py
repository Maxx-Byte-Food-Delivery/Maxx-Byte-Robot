import pytest
from django.contrib.auth.models import User

@pytest.fixture
#makes user
def user(db):
  user = User.objects.create_user(username="johndoe", email= "johndoe@email.com", first_name="john", last_name="doe", password="psswrd123!")
  user.save()
  return user
#makes multiple users
def users(db):
  user1 = User.objects.create_user(username="johndoe", email= "johndoe@email.com", first_name="john", last_name="doe", password ="psswrd123!")
  user2 = User.objects.create_user(username="janedoe", email= "janedoe@email.com", first_name="jane", last_name="doe", password ="SomeG00dPasswor!d")
  user3 = User.objects.create_user(username="SomeUser", email= "someuser@email.com", first_name="some", last_name="user", password="G00dPassw0rd!")
  user1.save()
  user2.save()
  user3.save()
  return users