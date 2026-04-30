import pytest
from apps.models.payment import Payment
from django.db import IntegrityError

@pytest.mark.django_db
def test_payment_creation(create_payment):
    assert create_payment.method == 'card'
    assert create_payment.amount == 100.00
    assert create_payment.transaction_id == 'abc123'
    assert create_payment.status == 'pending'
    assert create_payment.created_at is not None

def test_payment_creation_no_method(create_orders):
    with pytest.raises(IntegrityError):
        create_payment = Payment.objects.create(order=create_orders[0], method=None, amount=100.00, transaction_id='abc123', status='pending')

def test_payment_creation_no_amount(create_orders):
    with pytest.raises(IntegrityError):
        create_payment = Payment.objects.create(order=create_orders[0], method='card', amount=None, transaction_id='abc123', status='pending')

def test_payment_creation_no_transaction_id(create_orders):
    with pytest.raises(IntegrityError):
        create_payment = Payment.objects.create(order=create_orders[0], method='card', amount=100.00, transaction_id=None, status='pending')

def test_payment_creation_no_status(create_orders):
    with pytest.raises(IntegrityError):
        create_payment = Payment.objects.create(order=create_orders[0], method='card', amount=100.00, transaction_id='abc123', status=None)