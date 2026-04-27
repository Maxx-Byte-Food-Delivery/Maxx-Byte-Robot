import pytest

@pytest.mark.django_db
def test_order_item_creation(order_item):
    assert order_item.order is not None
    assert order_item.item_name == "Test Product"
    assert order_item.quantity == 2
    assert order_item.price == 50.00