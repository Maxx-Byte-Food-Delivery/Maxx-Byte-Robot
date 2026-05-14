import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_user_logout_endpoint(api_client, users):
  api_client.force_authenticate(user=users[0])
  url = reverse('logout')
  response = api_client.post(url, format='json')
  
  assert response.status_code == 200
  assert response.data['message'] == "Logged out successfully"

@pytest.mark.django_db
def test_user_logout_as_admin(api_client, admin_users):
  api_client.force_authenticate(user=admin_users[0])
  url = reverse('logout')
  response = api_client.post(url, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "Logged out successfully"

@pytest.mark.django_db
def test_user_logout_endpoint_not_logged_in(api_client, users):
  url = reverse('logout')
  response = api_client.post(url, format='json')
  
  assert response.status_code == 401
  assert response.data['message'] == "You are not logged in"