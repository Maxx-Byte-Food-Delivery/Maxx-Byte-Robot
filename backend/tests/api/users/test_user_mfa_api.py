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

@pytest.mark.skip(reason="Requires custom logic to prevent disabling both MFA methods as admin")
def test_admin_disable_mfa(api_client, admin_users, admin_profiles):
  api_client.force_authenticate(user=admin_users[0])
  assert admin_profiles[0].mfa_methods['sms'] == False
  assert admin_profiles[0].mfa_methods['totp'] == True

  url = reverse('disable-2fa')
  data = {"method": "totp"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 403
  assert response.data['message'] == "At least one MFA method must be enabled for your account"

@pytest.mark.skip(reason="Requires custom logic to prevent disabling both MFA methods as admin")
def test_admin_disable_mfa_with_both_enabled(api_client, admin_users, admin_profiles):
  api_client.force_authenticate(user=admin_users[0])
  url = reverse('enable-sms-2fa')
  response = api_client.post(url, format='json')
  assert response.status_code == 200
  assert admin_profiles[0].mfa_methods['sms'] == True
  assert admin_profiles[0].mfa_methods['totp'] == True

  url = reverse('disable-2fa')
  data = {"method": "totp"}
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "totp method disabled"
  assert admin_profiles[0].mfa_methods['sms'] == True

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