import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# when unskipping these tests change @pytest.mark.skip to @pytest.mark.django_db
# make sure url = reverse('login') or reverse('change_password') matches the name of the url pattern for the order placement endpoint in the urls.py file

@pytest.mark.django_db
def test_user_login_endpoint(api_client, users):
  url = reverse('login')
  data = {"username": "johndoe", "password": "psswrd123!"}
  response = api_client.post(url, data, format='json')

  if response.status_code != 200:
    print(response.data) 

  assert response.status_code == 200

@pytest.mark.django_db
def test_user_login_endpoint_wrong_password(api_client, users):
  url = reverse('login')
  data = {"username": "johndoe", "password": "wrongpassword"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 401
  assert response.data['error'] == "Wrong password"

@pytest.mark.skip(reason = "Logout endpoint not yet implemented")
def test_user_logout_endpoint(api_client, users):
  api_client.force_authenticate(user=users[0])
  url = reverse('logout')
  response = api_client.post(url, format='json')
  
  assert response.status_code == 200
  assert response.data['message'] == "Logged out successfully"

@pytest.mark.skip(reason = "Logout endpoint not yet implemented")
def test_user_logout_endpoint_not_logged_in(api_client, users):
  url = reverse('logout')
  response = api_client.post(url, format='json')
  
  assert response.status_code == 401
  assert response.data['message'] == "You are not logged in"

@pytest.mark.skip(reason = "change password endpoint not yet implamented")
def test_user_chnage_password_endpoint(api_client, users):
  api_client.force_authenticate(user=users[0])
  url = reverse('change_password')
  data = {"old_password": "psswrd123!", "new_password": "newpsswrd123!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "password changed successfully"
  assert get_user_model().objects.get(username="johndoe").check_password("newpsswrd123!") == True

@pytest.mark.skip(reason = "change password endpoint not yet implamented")
def test_user_chnage_password_endpoint_not_logged_in(api_client, users):
  url = reverse('change_password')
  data = {"old_password": "psswrd123!", "new_password": "newpsswrd123!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 401
  assert response.data['message'] == "You are not logged in"

@pytest.mark.skip(reason = "change password endpoint not yet implamented")
def test_user_chnage_password_endpoint_wrong_user(api_client, users):
  api_client.force_authenticate(user=users[0])

  url = reverse('change_password')
  data = {"old_password": "psswrd123!", "new_password": "newpsswrd123!", "user_id": users[1].id}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 403
  assert response.data['message'] == "Action not allowed"
