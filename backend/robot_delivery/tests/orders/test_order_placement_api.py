import pytest
from django.urls import reverse

#user can place an order successfully
@pytest.mark.skip(reason="order endpoint not yet implemented")
def test_order_placement(api_client, users, create_products):
    api_client.force_authenticate(user=users[0])

    url = reverse('place_order')
    data = {
        "items": [
            {"product_id": create_products[0].id, "quantity": 2},
            {"product_id": create_products[1].id, "quantity": 1}
        ]
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['message'] == "Order placed successfully"
    assert 'order_id' in response.data
    assert response.data['total_price'] == str(create_products[0].price * 2 + create_products[1].price)

#user cannot place an order without quantity
@pytest.mark.skip(reason="order endpoint not yet implemented")
def test_order_placement_no_quantity(api_client, users, create_products):
    api_client.force_authenticate(user=users[0])

    url = reverse('place_order')
    data = {
        "items": [
            {"product_id": create_products[0].id},
            {"product_id": create_products[1].id, "quantity": 1}
        ]
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == 400
    assert 'quantity' in response.data['error']

#user cannot place an order without logging in
@pytest.mark.skip(reason="order endpoint not yet implemented")
def test_order_placement_unauthenticated(api_client, create_products):
    url = reverse('place_order')
    data = {
        "items": [
            {"product_id": create_products[0].id, "quantity": 2},
            {"product_id": create_products[1].id, "quantity": 1}
        ]
    }
    response = api_client.post(url, data, format='json')

    assert response.status_code == 401
    assert response.data['detail'] == "Authentication credentials were not provided."