import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_order_history_endpoint(api_client, users, order_items, create_orders):
  api_client.force_authenticate(user=users[0])

  url = reverse('view_history')
  response = api_client.get(url, format='json')

  assert response.status_code == 200
  assert len(response.data) == 2
  assert response.data[0]['id'] == order_items[0].order.id
  assert float(response.data[0]['total_price']) == 39.98

@pytest.mark.django_db
def test_order_history_endpoint_user_cant_access_other_users_history(api_client, users, order_items):
  api_client.force_authenticate(user=users[1])
    
  # 2. TARGET: An order item belonging strictly to John Doe (users[0])
  # Assume order_items[0] is linked to an order owned by John Doe
  other_user_order_item_id = 1 
  
  # Resolves to: /api/orders/view_history/item/1/
  url = reverse('view_history_item', kwargs={'id': other_user_order_item_id}) 
  response = api_client.get(url, format='json')
  
  # 3. Assert that a 404 is thrown (our updated view uses .get() which throws DoesNotExist)
  assert response.status_code == 404

@pytest.mark.django_db
def test_order_history_endpoint_unauthenticated(api_client, users, order_items):
  url = reverse('view_history')
  response = api_client.get(url, format='json')

  assert response.status_code == 401
  assert response.data['error'] == 'You must be logged in to view order history'
  assert response.data['orders'] == []

@pytest.mark.django_db
def test_order_history_item_endpoint(api_client, users, order_items, create_orders):
  api_client.force_authenticate(user=users[0])

  url = reverse('view_history_item', args=[order_items[0].order.id])
  response = api_client.get(url, format='json')

  assert response.status_code == 200
  assert response.data['order_id'] == order_items[0].order.id
  assert len(response.data['items']) == 1
  assert response.data['items'][0]['product_name'] == "Test Product 1"
  assert response.data['items'][0]['quantity'] == 2
  assert float(response.data['items'][0]['price']) == float(19.99)
 
@pytest.mark.django_db
def test_order_history_item_endpoint_wrong_user(api_client, users, order_items):
  api_client.force_authenticate(user=users[1])

  url = reverse('view_history_item', args=[order_items[0].order.id])
  response = api_client.get(url, format='json')

  assert response.status_code == 404