import re
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.django_db(transaction = True)
def test_login(page: Page, live_server, users, create_orders):

  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))

  page.goto("http://localhost:5173/orders")

  page.wait_for_load_state("networkidle")

  order_card = page.get_by_text(f"Order ID: #{create_orders[0].id}")

  raw_price = create_orders[0].total_price
  formatted_price = int(raw_price) if float(raw_price).is_integer() else raw_price

  expect(order_card).to_contain_text(f"Total: ${formatted_price}")