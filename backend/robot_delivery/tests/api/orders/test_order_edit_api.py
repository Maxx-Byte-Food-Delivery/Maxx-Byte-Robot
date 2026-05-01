import pytest
from django.urls import reverse

# when unskipping these tests change @pytest.mark.skip to @pytest.mark.django_db
# make sure url = reverse('edit_order') matches the name of the url pattern for the order placement endpoint in the urls.py file

#user can edit an order successfully
@pytest.mark.skip(reason="edit order endpoint not yet implemented")
def test_order_edit(api_client, users, create_orders):
  api_client.force_authenticate(user=users[0])

  assert response.data['items'][0]['quantity'] == 2

  url = reverse('edit_order', args=[create_orders[0].id,users[0].id])
  data = {
    "items": [
      {"product_id": create_products[0].id, "quantity": 1},
      {"product_id": create_products[1].id, "quantity": 1}
    ]
  }
  response = api_client.post(url, data, format='json')

  assert response.status_code == 200
  assert response.data['message'] == "Order edited successfully"
  assert 'order_id' in response.data
  assert response.data['total_price'] == str(create_products[0].price * 1 + create_products[1].price)
  assert response.data['items'][0]['quantity'] == 1
  assert response.data['items'][1]['quantity'] == 1

@pytest.mark.skip(reason="edit order endpoint not yet implemented")
def test_order_edit_unauthenticated(api_client, create_orders):
  assert response.data['items'][0]['quantity'] == 2

  url = reverse('edit_order')
  data = {
    "items": [
      {"product_id": create_products[0].id, "quantity": 1},
      {"product_id": create_products[1].id, "quantity": 1}
    ]
  }
  response = api_client.post(url, data, format='json')

  assert response.status_code == 403
  assert response.data['message'] == "You must be logged in to edit this order"
  assert 'order_id' in response.data
  assert response.data['total_price'] == str(create_products[0].price * 1 + create_products[1].price)
  assert response.data['items'][0]['quantity'] == 2
  assert response.data['items'][1]['quantity'] == 1

@pytest.mark.skip(reason="edit order endpoint not yet implemented")
def test_order_edit_different_user(api_client, users, create_orders):
  api_client.force_authenticate(user=users[1])

  assert response.data['items'][0]['quantity'] == 2

  url = reverse('edit_order', args=[create_orders[0].id, users[1].id])
  data = {
    "items": [
      {"product_id": create_products[0].id, "quantity": 1},
      {"product_id": create_products[1].id, "quantity": 1}
    ]
  }
  response = api_client.post(url, data, format='json')

  assert response.status_code == 403
  assert response.data['message'] == "Action not allowed"
  assert 'order_id' in response.data
  assert response.data['total_price'] == str(create_products[0].price * 1 + create_products[1].price)
  assert response.data['items'][0]['quantity'] == 2
  assert response.data['items'][1]['quantity'] == 1
