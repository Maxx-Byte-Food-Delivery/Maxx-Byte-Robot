import re
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.django_db(transaction = True)
def test_add_products_to_cart(page: Page, live_server, users, create_products):
  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))
  page.wait_for_load_state("networkidle")

  page.get_by_role("link", name="Products").click()
  page.wait_for_load_state("networkidle")

  page.get_by_role("heading", name=create_products[0].name, exact=True).locator("xpath=./..").get_by_role("button", name="Add to Cart").click(force=True)

  page.get_by_role("link", name=re.compile(r"\d+")).click()
  page.wait_for_load_state("networkidle")

  expect(
    page.locator("p", has_text=f"{create_products[0].name} x1")
  ).to_be_visible()


