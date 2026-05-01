import pytest
from django.urls import reverse

# when unskipping these tests change @pytest.mark.skip to @pytest.mark.django_db
# make sure url = reverse('order_tracking') matches the name of the url pattern for the order placement endpoint in the urls.py file

#user can place an order successfully
@pytest.mark.skip(reason="order tracking endpoint not yet implemented")
def test_order_tracking_api_endpoint(api_client, users, create_orders):
  api_client.force_authenticate(user=users[0])

  url = reverse('order_tracking', args=[create_orders[0].id, users[0].id])
  response = api_client.get(url)

  assert response.status_code == 200
  assert response.data['status'] == "pending"
  assert response.data['eta'] == "10 minutes"
  assert response.data['destination'] == "2 miles"

@pytest.mark.skip(reason="order tracking endpoint not yet implemented")
def test_order_tracking_api_endpoint_unauthenticated(api_client, create_orders):
  url = reverse('order_tracking', args=[create_orders[0].id])
  response = api_client.get(url)

  assert response.status_code == 403
  assert response.data['detail'] == "This request requires you to be logged in."

@pytest.mark.skip(reason="order tracking endpoint not yet implemented")
def test_order_tracking_api_endpoint_no_order(api_client, create_orders):
  url = reverse('order_tracking', args=[users[1].id])
  response = api_client.get(url)

  assert response.status_code == 400
  assert response.data['detail'] == "This request requires an order"