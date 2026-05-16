import re
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.django_db
def test_login(page: Page, live_server, users):

  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))
