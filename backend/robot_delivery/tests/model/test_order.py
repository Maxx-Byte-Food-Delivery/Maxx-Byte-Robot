import pytest
from apps.models.order import Order
from django.db import IntegrityError

@pytest.mark.django_db
def test_user_place_order(create_order):
    assert create_order.total_price == 100.00
    assert create_order.status == 'pending'
    assert create_order.created_at is not None

def test_user_place_order_no_total_price(user):
    with pytest.raises(IntegrityError):
        create_order = Order.objects.create(user=user, total_price=None)

def test_user_place_order_no_status(user):
    with pytest.raises(IntegrityError):
        create_order = Order.objects.create(user=user, total_price=100.00, status=None)