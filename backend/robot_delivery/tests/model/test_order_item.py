import pytest
from apps.models.order import Order
from apps.models.order_item import OrderItem
from django.db import IntegrityError

@pytest.mark.django_db
def test_order_item_creation(order_item):
    assert order_item.order is not None
    assert order_item.product is not None
    assert order_item.product.name == "Test Product 1"
    assert order_item.quantity == 2
    assert order_item.price == 50.00

@pytest.mark.django_db
def test_order_item_creation_no_quantity(create_order, create_products):
    with pytest.raises(IntegrityError):
        order_item = OrderItem.objects.create(order=create_order, product=create_products[0], quantity=None, price=50.00)
        
@pytest.mark.django_db
def test_order_item_creation_no_price(create_order, create_products):
    with pytest.raises(IntegrityError):
        order_item = OrderItem.objects.create(order=create_order, product=create_products[0], quantity=2, price=None)   