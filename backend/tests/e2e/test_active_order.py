import re
from playwright.sync_api import Page, expect
import pytest
## replace skip(reason="") with django_db(transaction = True)
@pytest.mark.django_db(transaction = True)
def test_active_orders(page: Page, live_server, users, create_orders, run_react_frontend):
  create_orders[0].status = "active"
  create_orders[0].save()

  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))

  page.goto("http://localhost:5173/orders/active")
  page.wait_for_load_state("networkidle")

  expect(
    page.locator("p", has_text=f"Status: active")
  ).to_be_visible()

  expect(
    page.locator("h3", has_text=f"Order #{create_orders[0].id}")
  ).to_be_visible()

@pytest.mark.django_db(transaction = True)
def test_active_orders_none(page: Page, live_server, users, create_orders, run_react_frontend):

  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))

  page.goto("http://localhost:5173/orders/active")
  page.wait_for_load_state("networkidle")

  expect(
    page.locator("p", has_text=f"Status: active")
  ).not_to_be_visible()

  expect(
    page.locator("h3", has_text=f"Order #{create_orders[0].id}")
  ).not_to_be_visible()

@pytest.mark.skip(reason="not yet implemented")
def test_active_order(page: Page, live_server, users, create_orders, run_react_frontend):
  create_orders[0].status = "active"
  create_orders[0].save()

  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))

  page.goto("http://localhost:5173/orders/active/{create_orders[0].id}")
  page.wait_for_load_state("networkidle")

  expect(
    page.locator("p", has_text=f"Status: active")
  ).to_be_visible()

  expect(
    page.locator("h3", has_text=f"Order #{create_orders[0].id}")
  ).to_be_visible()

@pytest.mark.skip(reason="not yet implemented")
def test_active_order_wrong_user(page: Page, live_server, users, create_orders, run_react_frontend):
  create_orders[1].status = "active"
  create_orders[1].save()

  page.goto("http://localhost:5173/")
  page.get_by_placeholder("Username").fill("johndoe")
  page.get_by_placeholder("Password").fill("VeryG00d!Password")
  page.get_by_role("button", name="Login").click()
  
  expect(page).to_have_url(re.compile(r"/student"))

  page.goto("http://localhost:5173/orders/active/{create_orders[1].id}")
  page.wait_for_load_state("networkidle")

  expect(
    page.locator("p", has_text=f"Status: active")
  ).not_to_be_visible()

  expect(
    page.locator("h3", has_text=f"Order #{create_orders[0].id}")
  ).not_to_be_visible()
  
