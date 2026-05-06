import pytest
from django.urls import reverse
import pyotp

@pytest.mark.django_db
def test_user_login_endpoint_mfa_totp_as_admin(api_client, admin_users, admin_profiles):
  url = reverse('login')
  data = {"username": "admin", "password": "AdminP@ssw0rd!"}
  response = api_client.post(url, data, format='json')

  if response.status_code != 200:
    print(response.data) 

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "totp"
  assert response.data['role'] == "staff"

  url = reverse('verify-mfa')
  totp = pyotp.TOTP(admin_profiles[0].mfa_secret)
  code = totp.now()
  data = {"code": code}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "MFA verified"

@pytest.mark.django_db
def test_user_login_endpoint_mfa_totp_as_admin_wrong_code(api_client, admin_users, admin_profiles):
  url = reverse('login')
  data = {"username": "admin", "password": "AdminP@ssw0rd!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "totp"
  assert response.data['role'] == "staff"

  url = reverse('verify-mfa')
  data = {"code": "000000"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 400
  assert response.data['message'] == "Invalid code"

@pytest.mark.django_db
def test_user_login_endpoint_sms_as_admin(api_client, admin_users, admin_profiles):
  url = reverse('login')
  data = {"username": "admin2", "password": "AdminP@ssw0rd!"}
  response = api_client.post(url, data, format='json')

  if response.status_code != 200:
    print(response.data) 

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "sms"
  assert response.data['role'] == "staff"

  url = reverse('verify-mfa')
  admin_profiles[1].refresh_from_db()
  code = admin_profiles[1].mfa_code
  data = {"code": code}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "MFA verified"

@pytest.mark.django_db
def test_user_login_endpoint_sms_as_admin_wrong_code(api_client, admin_users, admin_profiles):
  url = reverse('login')
  data = {"username": "admin2", "password": "AdminP@ssw0rd!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "sms"
  assert response.data['role'] == "staff"

  url = reverse('verify-mfa')
  data = {"code": "000000"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 400
  assert response.data['message'] == "Invalid code"

@pytest.mark.django_db
def test_user_login_endpoint_mfa_totp_as_student(api_client, users, student_profiles):
  url = reverse('login')
  data = {"username": "SomeUser", "password": "G00dPassw0rd!"}
  response = api_client.post(url, data, format='json')

  if response.status_code != 200:
    print(response.data) 

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "totp"
  assert response.data['role'] == "student"

  url = reverse('verify-mfa')
  totp = pyotp.TOTP(student_profiles[0].mfa_secret)
  code = totp.now()
  data = {"code": code}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "MFA verified"

@pytest.mark.django_db
def test_user_login_endpoint_mfa_totp_as_student_wrong_code(api_client, users, student_profiles):
  url = reverse('login')
  data = {"username": "SomeUser", "password": "G00dPassw0rd!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "totp"
  assert response.data['role'] == "student"

  url = reverse('verify-mfa')
  data = {"code": "000000"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 400
  assert response.data['message'] == "Invalid code"

@pytest.mark.django_db
def test_user_login_endpoint_sms_as_student(api_client, users, student_profiles):
  url = reverse('login')
  data = {"username": "student", "password": "StudentP@ssw0rd!"}
  response = api_client.post(url, data, format='json')

  if response.status_code != 200:
    print(response.data) 

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "sms"
  assert response.data['role'] == "student"

  url = reverse('verify-mfa')
  student_profiles[1].refresh_from_db()
  code = student_profiles[1].mfa_code
  data = {"code": code}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "MFA verified"

@pytest.mark.django_db
def test_user_login_endpoint_sms_as_student_wrong_code(api_client, users, student_profiles):
  url = reverse('login')
  data = {"username": "student", "password": "StudentP@ssw0rd!"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['requires_2fa'] == True
  assert response.data['method'] == "sms"
  assert response.data['role'] == "student"

  url = reverse('verify-mfa')
  data = {"code": "000000"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 400
  assert response.data['message'] == "Invalid code"