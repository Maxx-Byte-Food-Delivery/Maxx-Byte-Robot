import pytest
from django.urls import reverse

# when unskipping these tests change @pytest.mark.skip to @pytest.mark.django_db
# make sure url = reverse('cancel_order') matches the name of the url pattern for the order placement endpoint in the urls.py file

#user can cancel an order successfully
@pytest.mark.skip(reason="cancel order endpoint not yet implemented")
def test_order_cancel_api_endpoint(api_client, users, create_orders):
  api_client.force_authenticate(user=users[0])

  url = reverse('cancel_order', args=[create_orders[0].id,users[0].id])
  response = api_client.post(url)

  assert response.status_code == 200
  assert response.data['message'] == "Order cancelled successfully"
  assert 'order_id' in response.data
  assert response.data['order_id'] == create_orders[0].id
  assert response.data['status'] == "cancelled"

@pytest.mark.skip(reason="cancel order endpoint not yet implemented")
def test_cant_cancel_other_user_order_api_endpoint(api_client, users, create_orders):
  api_client.force_authenticate(user=users[0])

  url = reverse('cancel_order', args=[create_orders[1].id,users[0].id])
  response = api_client.post(url)

  assert response.status_code == 403
  assert response.data['message'] == "Action not allowed."
  assert 'order_id' not in response.data
  assert create_orders[1].status != "cancelled"

@pytest.mark.skip(reason="cancel order endpoint not yet implemented")
def test_cant_cancel_order_not_authenticated(api_client, users, create_orders):
  url = reverse('cancel_order', args=[create_orders[0].id, users[0].id])
  response = api_client.post(url)

  assert response.status_code == 403
  assert response.data['message'] == "To cancel an order you must be logged in."
  assert 'order_id' not in response.data
  assert create_orders[0].status != "cancelled"

@pytest.mark.skip(reason="cancel order endpoint not yet implemented")
def test_order_cancel_api_endpoint_no_order(api_client, users, create_orders):
  api_client.force_authenticate(user=users[0])

  url = reverse('cancel_order', args=[users[0].id])
  response = api_client.post(url)

  assert response.status_code == 404
  assert response.data['message'] == "Order not found."

  assert 'order_id' not in response.data
  assert create_orders[0].status != "cancelled"