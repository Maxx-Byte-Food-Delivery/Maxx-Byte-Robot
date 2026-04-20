import pytest
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_user_creation(user):
  assert user is not None

#test for that username is not blank
@pytest.mark.django_db
def test_user_username_cant_be_blank():
 with pytest.raises(ValueError, match="The given username must be set"):
  User.objects.create_user(username="", email="johndoe@email.com", password="password")


#test that user cant be created without password
@pytest.mark.django_db
def test_user_password_cant_be_blank():
 with pytest.raises(ValueError, match="Password must be set"):
  User.objects.create_user(username="john doe", email="johndoe@email.com", password="")

#test that user can't be created without email
@pytest.mark.django_db
def test_user_email_cant_be_blank():
 with pytest.raises(ValueError, match="Email must be set"):
  User.objects.create_user(username="john doe", email="", password="password")

# @pytest.mark.django_db
# def test_user_not_admin_by_default(user):
#   assert user.username == "john doe"
#   assert user.admin == False