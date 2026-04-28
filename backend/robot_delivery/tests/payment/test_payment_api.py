import pytest
from django.urls import reverse
from apps.models import Payment

@pytest.mark.django_db
def test_payment_endpoint(api_client, user, create_order):
  url = reverse("create_checkout_session")

  data = {"order": create_order.id, "user": user.id, "total_price": create_order.total_price, "status": "pending"}
  response = api_client.post(url, data, format="json")

  if response.status_code != 200:
    print(response.data)

  assert response.status_code == 200
  payment = Payment.objects.filter(order=create_order).first()
  assert payment is not None
  assert payment.status == "pending"
  assert float(payment.amount) == 100.00
  assert payment.order.user == create_order.user

def test_payment_endpoint_missing_order(api_client, create_order):
  url = reverse("create_checkout_session")
  data = {"total_price": create_order.total_price, "status": "pending"}
  response = api_client.post(url, data, format="json")

  assert response.status_code == 400
  assert "error" in response.data
  assert response.data["error"] == "order_id is required"

@pytest.mark.django_db
def test_payment_endpoint_invalid_order(api_client, create_order):
  url = reverse("create_checkout_session")
  data = {"order": 9999, "total_price": create_order.total_price, "status": "pending"}
  response = api_client.post(url, data, format="json")

  assert response.status_code == 404
  assert "error" in response.data
  assert response.data["error"] == "Order not found"