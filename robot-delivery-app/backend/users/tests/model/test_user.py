import pytest
from django.contrib.auth.hashers import check_password

@pytest.mark.django_db
def test_user_creation(user):
  assert user is not None

@pytest.mark.django_db
def test_user_password_hashed(user):
  assert user.username == "john doe"
  assert check_password("psswrd123", user.password)

#test for that username is valid
#def test_user_has_valid_username


#test that user cant be created without password

#test that user cant be created without username

#@pytest.mark.django_db
#def test_user_not_admin_by_default(user):
  #assert user.username == "john doe"
  #assert user.admin == False