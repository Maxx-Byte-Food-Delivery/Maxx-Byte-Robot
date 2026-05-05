import pytest
from apps.models.order import Order
from apps.models.order_item import OrderItem
from django.db import IntegrityError

@pytest.mark.django_db
def test_order_item_creation(order_items):
    assert order_items[0].order is not None
    assert order_items[0].product is not None
    assert order_items[0].product.name == "Test Product 1"
    assert order_items[0].quantity == 2

@pytest.mark.django_db
def test_order_item_creation_no_quantity(create_orders, create_products):
    with pytest.raises(IntegrityError):
        order_item = OrderItem.objects.create(order=create_orders[0], product=create_products[0], quantity=None) 