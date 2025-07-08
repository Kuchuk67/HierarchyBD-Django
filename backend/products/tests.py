from rest_framework import status


def test_products_created(api_client, create_test_data):
    response = api_client.get("/api/v1/products")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 2


def test_patch(api_client, create_test_data, product_one, product_patch):
    """
    Тест на изменение продукта PATCH
    """
    response = api_client.post(
        path=f"/api/v1/products", data=product_one, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    id_product = response.data["id"]

    rezult = dict(
        {
            "id": id_product,
            "name_product": "Продукт изменен",
            "model_product": "Модель продукта 2",
            "release_date": "2024-07-07",
        }
    )
    response = api_client.patch(
        path=f"/api/v1/products/{id_product}", data=product_patch, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == rezult

    response = api_client.get(path=f"/api/v1/products/{id_product}")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == rezult


def test_put(api_client, create_test_data, product_one, product_put):
    """
    Тест на изменение продукта PUT
    """
    response = api_client.post(
        path=f"/api/v1/products", data=product_one, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    id_product = response.data["id"]

    rezult = dict(
        {
            "id": id_product,
            "name_product": "Продукт 11",
            "model_product": "Модель продукта 11",
            "release_date": "2025-07-07",
        }
    )
    response = api_client.put(
        path=f"/api/v1/products/{id_product}", data=product_put, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == rezult

    response = api_client.get(path=f"/api/v1/products/{id_product}")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == rezult
