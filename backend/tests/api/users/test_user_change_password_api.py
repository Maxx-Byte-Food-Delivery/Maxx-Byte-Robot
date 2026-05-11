import pytest
from django.urls import reverse
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError

# when unskipping these tests change @pytest.mark.skip to @pytest.mark.django_db
# make sure url = reverse('change_password') matches the name of the url pattern for the user change password endpoint in the urls.py file

@pytest.mark.skip(reason = "change password endpoint not yet implamented")
def test_user_change_password_endpoint(api_client, users):
  api_client.force_authenticate(user=users[0])
  url = reverse('change_password')
  data = {"old_password": "VeryG00d!Password", "new_password": "Som3NewG00dP!assword"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "password changed successfully"
  assert get_user_model().objects.get(username="johndoe").check_password("Som3NewG00dP!assword") == True

@pytest.mark.skip(reason = "change password endpoint not yet implamented")
def test_user_change_password_endpoint_weak_password(api_client, users):
  api_client.force_authenticate(user=users[0])
  
  with pytest.raises(ValidationError) as excinfo:
    url = reverse('change_password')
    data = {"old_password": "VeryG00d!Password", "new_password": "password"}
    response = api_client.post(url, data, format='json')
  assert "This password is too common." in str(excinfo.value)
  

@pytest.mark.skip(reason = "change password endpoint not yet implamented")
def test_user_change_password_endpoint_not_logged_in(api_client, users):
  url = reverse('change_password')
  data = {"old_password": "psswrd123!", "new_password": "newpsswrd123!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 401
  assert response.data['message'] == "You are not logged in"

@pytest.mark.skip(reason = "change password endpoint not yet implamented")
def test_user_change_password_endpoint_wrong_user(api_client, users):
  api_client.force_authenticate(user=users[0])

  url = reverse('change_password')
  data = {"old_password": "psswrd123!", "new_password": "newpsswrd123!", "user_id": users[1].id}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 403
  assert response.data['message'] == "Action not allowed"