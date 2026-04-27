import pytest
from apps.models import payment

@pytest.mark.django_db
def test_payment_creation(create_payment):
    assert create_payment.method == 'card'
    assert create_payment.amount == 100.00
    assert create_payment.transaction_id == 'abc123'
    assert create_payment.status == 'pending'
    assert create_payment.created_at is not None