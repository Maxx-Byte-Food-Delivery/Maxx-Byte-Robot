import pytest
from django.urls import reverse
from apps.models.product import Product

@pytest.mark.django_db
def test_product_endpoint(api_client, create_products):
  url = reverse("get_all_products")
  response = api_client.get(url, format="json")

  if response.status_code != 200:
    print(response.data)

  assert response.status_code == 200
  assert response.data is not None
  assert response.data["products"][0]["name"] == "Test Product 1"
  assert float(response.data["products"][0]["price"]) == 19.99
  assert response.data["products"][0]["description"] == "Description for Test Product 1"
  assert response.data["products"][1]["name"] == "Test Product 2"
  assert float(response.data["products"][1]["price"]) == 29.99
  assert response.data["products"][1]["description"] == "Description for Test Product 2"