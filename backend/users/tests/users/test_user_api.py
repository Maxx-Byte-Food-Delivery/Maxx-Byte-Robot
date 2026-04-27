import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_user_login_endpoint(api_client, user):
  url = reverse('login')
  data = {"username": "johndoe", "password": "psswrd123!"}
  response = api_client.post(url, data, format='json')

  if response.status_code != 200:
    print(response.data) 

  assert response.status_code == 200

@pytest.mark.django_db
def test_user_login_endpoint_wrong_password(api_client, user):
  url = reverse('login')
  data = {"username": "johndoe", "password": "wrongpassword"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 401
  assert response.data['error'] == "Wrong password"