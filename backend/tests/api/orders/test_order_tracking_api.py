import pytest
from django.urls import reverse

# when unskipping these tests change @pytest.mark.skip to @pytest.mark.django_db
# make sure url = reverse('order_tracking') matches the name of the url pattern for the order tracking endpoint in the urls.py file

#user can place an order successfully
@pytest.mark.django_db
def test_order_tracking_api_endpoint(api_client, users, create_orders, order_items):
  api_client.force_authenticate(user=users[0])
  create_orders[0].status = "active"
  create_orders[0].save()
  
  url = reverse('active_order', kwargs={'order_id': create_orders[0].id})
  response = api_client.get(url, format='json')
  assert response.status_code == 200
  assert response.data['status'] == "active"
  assert response.data['id'] == create_orders[0].id
  assert float(response.data['total_price']) == float(39.98)
  # assert response.data['eta'] == "10 minutes"
  # assert response.data['destination'] == "2 miles"

@pytest.mark.django_db
def test_order_tracking_api_endpoint_unauthenticated(api_client, create_orders, users):
  create_orders[0].status = "active"
  create_orders[0].save()

  url = reverse('active_order', kwargs={'order_id': create_orders[0].id})
  response = api_client.get(url)
  
  assert response.status_code == 403
  assert response.data['detail'] == "Authentication credentials were not provided."

@pytest.mark.django_db
def test_order_tracking_api_endpoint_wrong_user(api_client, create_orders, users):
  api_client.force_authenticate(user=users[0])
  create_orders[0].status = "active"
  create_orders[0].save()

  url = reverse('active_order', kwargs={'order_id': create_orders[1].id})
  response = api_client.get(url)

  assert response.status_code == 404
  assert response.data['error'] == "Active order not found"

@pytest.mark.django_db
def test_orders_tracking_api_endpoint(api_client, users, create_orders, order_items):
  api_client.force_authenticate(user=users[0])
  create_orders[0].status = "active"
  create_orders[0].save()
  assert create_orders[0].user.id == users[0].id
  assert create_orders[3].user.id == users[0].id
  assert create_orders[3].status == "pending"

  url = reverse('active_orders')
  
  response = api_client.get(url)

  assert response.status_code == 200
  assert len(response.data) == 1
  assert response.data[0]['status'] == "active"
  assert response.data[0]['id'] == create_orders[0].id
  assert float(response.data[0]['total_price']) == float(39.98)


@pytest.mark.django_db
def test_orders_tracking_api_endpoint_unauthenticated(api_client, create_orders, users):
  create_orders[0].status = "active"
  create_orders[0].save()

  url = reverse('active_orders')
  response = api_client.get(url)
  
  assert response.status_code == 403
  assert response.data['detail'] == "Authentication credentials were not provided."

@pytest.mark.django_db
def test_orders_tracking_api_endpoint_no_order(api_client, create_orders, admin_users):
  api_client.force_authenticate(user=admin_users[1])
  url = reverse('active_orders')
  response = api_client.get(url)

  assert response.status_code == 200
  assert response.json()['message'] == "No Active Orders"