import pytest
from apps.models.order import Order
from apps.models.order_item import OrderItem
from django.db import IntegrityError

@pytest.mark.django_db
def test_order_item_creation(order_item):
    assert order_item.order is not None
    assert order_item.item_name == "Test Product"
    assert order_item.quantity == 2
    assert order_item.price == 50.00

def test_order_item_creation_no_item_name(create_order):
    with pytest.raises(IntegrityError):
        order_item = OrderItem.objects.create(item_name=None, quantity=2, price=50.00)

def test_order_item_creation_no_quantity(create_order):
    with pytest.raises(IntegrityError):
        order_item = OrderItem.objects.create(item_name="Test Product", quantity=None, price=50.00)

def test_order_item_creation_no_price(create_order):
    with pytest.raises(IntegrityError):
        order_item = OrderItem.objects.create(item_name="Test Product", quantity=2, price=None)