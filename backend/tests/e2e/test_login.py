import re
from playwright.sync_api import Page, expect
import pytest
import pyotp

@pytest.mark.django_db
def test_login_as_user(page: Page, live_server, users):

  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))

@pytest.mark.django_db(transaction = True)
def test_login_as_admin_totp(page: Page, live_server, admin_users, admin_profiles):

  page.goto("http://localhost:5173/")

  page.get_by_placeholder("Username").fill("admin")
  page.get_by_placeholder("Password").fill("AdminP@ssw0rd!")

  page.get_by_role("button", name="Login").click()
  page.wait_for_load_state("networkidle")

  expect(page.get_by_text("Invalid username or password")).not_to_be_visible()
  
  expect(page).to_have_url(re.compile(r"/verify-totp"))

  totp = pyotp.TOTP(admin_profiles[0].mfa_secret)
  code = totp.now()
  print(admin_profiles[0].mfa_secret)
  page.get_by_placeholder("6-digit code").fill(code)

  page.get_by_role("button", name="Verify").click()
  page.wait_for_load_state("networkidle")

  expect(page).to_have_url(re.compile(r"/staff"))

@pytest.mark.django_db(transaction = True)
def test_login_as_admin_sms(page: Page, live_server, admin_users, admin_profiles):

  page.goto("http://localhost:5173/")

  page.get_by_placeholder("Username").fill("admin2")
  page.get_by_placeholder("Password").fill("AdminP@ssw0rd!")

  page.get_by_role("button", name="Login").click()
  page.wait_for_load_state("networkidle")

  expect(page.get_by_text("Invalid username or password")).not_to_be_visible()

  expect(page).to_have_url(re.compile(r"/verify-sms"))

  target_user = admin_users[1]
    
  target_user.refresh_from_db()

  fresh_sms_code = target_user.profile.mfa_code

  data = {"code": fresh_sms_code}
  
  page.get_by_placeholder("6-digit code").fill(data["code"])

  page.get_by_role("button", name="Verify").click()
  page.wait_for_load_state("networkidle")

  expect(page).to_have_url(re.compile(r"/staff"))

