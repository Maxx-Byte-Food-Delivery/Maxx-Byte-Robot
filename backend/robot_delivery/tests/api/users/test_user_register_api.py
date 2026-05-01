import pytest
from django.urls import reverse

# when unskipping these tests change @pytest.mark.skip to @pytest.mark.django_db
# make sure url = reverse('place_order') matches the name of the url pattern for the order placement endpoint in the urls.py file

@pytest.mark.skip(reason="no user registration api endpoint yet")
def test_user_registration_api_endpoint(api_client):
  url = reverse('register')
  data = {
    "username": "john_doe",
    "email": "johndoe@eail.com",
    "password": "G00dPassw0rd!",
    "first_name": "John",
    "last_name": "Doe"
  }
  response = api_client.post(url, data, format='json')

  assert response.status_code == 201

@pytest.mark.skip(reason="no user registration api endpoint yet")
def test_user_registration_api_endpoint_without_email(api_client):
  url = reverse('register')
  data = {
    "username": "john_doe",
    "email": "",
    "password": "G00dPassw0rd!",
    "first_name": "John",
    "last_name": "Doe"
  }

  assert api_client.post(url, data, format='json').status_code == 400
  assert api_client.post(url, data, format='json').data['email'][0] == 'Email must be set'

@pytest.mark.skip(reason="no user registration api endpoint yet")
def test_user_registration_api_endpoint_without_username(api_client):
  url = reverse('register')
  data = {
    "username": "",
    "email": "johndoe@email.com",
    "password": "G00dPassw0rd!",
    "first_name": "John",
    "last_name": "Doe"
  }

  assert api_client.post(url, data, format='json').status_code == 400
  assert api_client.post(url, data, format='json').data['username'][0] == 'Username must be set'

@pytest.mark.skip(reason="no user registration api endpoint yet")
def test_user_registration_api_endpoint_without_password(api_client):
  url = reverse('register')
  data = {
    "username": "john_doe",
    "email": "johndoe@email.com",
    "password": "",
    "first_name": "John",
    "last_name": "Doe"
  }

  assert api_client.post(url, data, format='json').status_code == 400
  assert api_client.post(url, data, format='json').data['password'][0] == 'Password must be set'