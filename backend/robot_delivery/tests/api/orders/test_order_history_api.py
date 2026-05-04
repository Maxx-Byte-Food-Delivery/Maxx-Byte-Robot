import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_order_history_endpoint(api_client, users, order_items):
  api_client.force_authenticate(user=users[0])

  url = reverse('view_history', args=[users[0].id])
  response = api_client.get(url, format='json')

  assert response.status_code == 200
  assert len(response.data) == 1
  assert response.data[0]['id'] == order_items[0].order.id
  assert float(response.data[0]['total_price']) == 39.98

@pytest.mark.django_db
def test_order_history_endpoint_user_cant_access_other_users_history(api_client, users, order_items):
  api_client.force_authenticate(user=users[1])

  url = reverse('view_history', args=[users[0].id])
  response = api_client.get(url, format='json')

  assert response.status_code == 403
  assert response.data['error'] == 'Unauthorized'

@pytest.mark.django_db
def test_order_history_item_endpoint(api_client, users, order_items):
  api_client.force_authenticate(user=users[0])

  url = reverse('view_history_item', args=[users[0].id, order_items[0].order.id])
  response = api_client.get(url, format='json')

  assert response.status_code == 200
  assert response.data['order']['id'] == order_items[0].order.id
  assert len(response.data['order_items']) == 1
  assert response.data['order_items'][0]['product']['name'] == "Test Product 1"
  assert response.data['order_items'][0]['quantity'] == 2
  assert float(response.data['order_items'][0]['price']) == 39.98
  assert float(response.data['order_items'][0]['product']['price']) == 19.99
 
@pytest.mark.django_db
def test_order_history_item_endpoint_wrong_user(api_client, users, order_items):
  api_client.force_authenticate(user=users[0])

  url = reverse('view_history_item', args=[users[1].id, order_items[0].order.id])
  response = api_client.get(url, format='json')

  assert response.status_code == 403
  assert response.data['error'] == 'Unauthorized'
