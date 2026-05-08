import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_user_login_endpoint(api_client, users):
  url = reverse('login')
  data = {"username": "johndoe", "password": "psswrd123!"}
  response = api_client.post(url, data, format='json')

  if response.status_code != 200:
    print(response.data) 

  assert response.status_code == 200
  assert response.data['requires_2fa'] == False
  assert response.data['role'] == "student"

@pytest.mark.django_db
def test_user_login_endpoint_wrong_password(api_client, users):
  url = reverse('login')
  data = {"username": "johndoe", "password": "wrongpassword"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 401
  assert response.data['error'] == "Invalid credentials"

@pytest.mark.django_db
def test_user_login_endpoint_no_username(api_client, users):
  url = reverse('login')
  data = {"username": "", "password": "psswrd123!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 401
  assert response.data['error'] == "Invalid credentials"
