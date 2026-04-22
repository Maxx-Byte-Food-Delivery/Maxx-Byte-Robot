import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_user_login_endpoint(api_client, user):
  url = reverse('/api/users/login')
  data = {"username": "johndoe", "password": "psswrd123!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200