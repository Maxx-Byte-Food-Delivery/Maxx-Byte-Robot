import pytest
from apps.models.order import Order
from django.db import IntegrityError

@pytest.mark.django_db
def test_user_place_order(create_orders):
    assert create_orders[0].total_price == 100.00
    assert create_orders[0].status == 'pending'
    assert create_orders[0].created_at is not None

def test_user_place_order_no_total_price(users):
    with pytest.raises(IntegrityError):
        create_order = Order.objects.create(user=users[0], total_price=None)

def test_user_place_order_no_status(users):
    with pytest.raises(IntegrityError):
        create_order = Order.objects.create(user=users[0], total_price=100.00, status=None)