import pytest
from django.urls import reverse
from apps.models import Payment
from unittest.mock import patch, MagicMock
import stripe

@pytest.mark.django_db
def test_payment_endpoint(api_client, create_orders, users):
  api_client.force_authenticate(user=users[0])

  url = reverse("create_checkout_session")

  data = {"order": create_orders[0].id, "user": users[0].id, }
  response = api_client.post(url, data, format="json")

  if response.status_code != 200:
    print(response.data)

  assert response.status_code == 200
  payment = Payment.objects.filter(order=create_orders[0]).first()
  assert payment is not None
  assert payment.status == "pending"
  assert float(payment.amount) == 100.00
  assert payment.order.user == create_orders[0].user

def test_payment_endpoint_missing_order(api_client, create_orders, users):
  api_client.force_authenticate(user=users[0])

  url = reverse("create_checkout_session")
  data = {"user": users[0].id}
  response = api_client.post(url, data, format="json")

  assert response.status_code == 400
  assert "error" in response.data
  assert response.data["error"] == "order_id is required"

@pytest.mark.django_db
def test_payment_endpoint_invalid_order(api_client, create_orders, users):
  api_client.force_authenticate(user=users[0])

  url = reverse("create_checkout_session")
  data = {"order": 9999, "user": users[0].id}
  response = api_client.post(url, data, format="json")

  assert response.status_code == 404
  assert "error" in response.data
  assert response.data["error"] == "Order not found"

@pytest.mark.django_db
@patch('stripe.checkout.Session.create')
@patch('stripe.Webhook.construct_event')
def test_stripe_webhook_checkout_completed(mock_construct_event, mock_session_create, api_client, create_orders, users):
    api_client.force_authenticate(user=users[0])

    mock_session = MagicMock()
    mock_session.id = 'cs_test_123'
    mock_session_create.return_value = mock_session

    url = reverse("create_checkout_session")
    data = {"order": create_orders[0].id, "user": users[0].id}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 200

    mock_event = {
      'type': 'checkout.session.completed',
      'data': {
        'object': {
          'id': 'cs_test_123',
          'metadata': {'order_id': str(create_orders[0].id)}
        }
      }
    }
    mock_construct_event.return_value = mock_event

    webhook_url = '/api/stripe/webhook'
    payload = b'fake_payload'
    response = api_client.post(webhook_url, payload, content_type='application/json', HTTP_STRIPE_SIGNATURE='fake_sig')

    assert response.status_code == 200

    create_orders[0].refresh_from_db()
    assert create_orders[0].status == 'confirmed'

@pytest.mark.django_db
@patch('stripe.checkout.Session.create')
@patch('stripe.Webhook.construct_event')
def test_stripe_webhook_invalid_signature(mock_construct_event, mock_session_create, api_client, create_orders, users):
    api_client.force_authenticate(user=users[0])

    mock_construct_event.side_effect = stripe.error.SignatureVerificationError("Invalid signature", None)

    mock_session = MagicMock()
    mock_session.id = 'cs_test_123'
    mock_session_create.return_value = mock_session

    url = reverse("create_checkout_session")
    data = {"order": create_orders[0].id, "user": users[0].id}
    response = api_client.post(url, data, format="json")

    webhook_url = '/api/stripe/webhook'
    payload = b'fake_payload'
    response = api_client.post(webhook_url, payload, content_type='application/json', HTTP_STRIPE_SIGNATURE='invalid_sig')

    assert response.status_code == 400

@pytest.mark.django_db
@patch('stripe.checkout.Session.create')
@patch('stripe.Webhook.construct_event')
def test_stripe_webhook_invalid_payload(mock_construct_event, mock_session_create, api_client, create_orders, users):
    api_client.force_authenticate(user=users[0])

    mock_construct_event.side_effect = ValueError("Invalid payload")

    mock_session = MagicMock()
    mock_session.id = 'cs_test_123'
    mock_session_create.return_value = mock_session

    url = reverse("create_checkout_session")
    data = {"order": create_orders[0].id, "user": users[0].id}
    response = api_client.post(url, data, format="json")

    webhook_url = '/api/stripe/webhook'
    payload = b'invalid_payload'
    response = api_client.post(webhook_url, payload, content_type='application/json', HTTP_STRIPE_SIGNATURE='fake_sig')

    assert response.status_code == 400

def test_stripe_webhook_user_cant_pay_for_other_users(api_client, create_orders, users):
    api_client.force_authenticate(user=users[0])

    url = reverse("create_checkout_session")
    data = {"order": create_orders[1].id, "user": users[1].id}
    response = api_client.post(url, data, format="json")
    assert response.status_code == 403
    assert response.data["error"] == "Action not allowed"
