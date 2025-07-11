from rest_framework import status
from .serializer import MoneyField
from decimal import Decimal


def test_money_field():
    """
    Тест - функции перевода суммы 
    из копеек в рубли и обратно
    """
    test_class = MoneyField()
    assert test_class.to_representation(1245) == Decimal('12.45')
    assert test_class.to_representation(4500) == Decimal('45.00')
    assert test_class.to_representation(45750) == Decimal('457.50')
    assert test_class.to_representation(5) == Decimal('0.05')

    assert test_class.to_internal_value('12.45') == 1245
    assert test_class.to_internal_value('45.00') == 4500
    assert test_class.to_internal_value('457.50') == 45750
    assert test_class.to_internal_value('0.05') == 5
    assert test_class.to_internal_value('10') == 1000
    assert test_class.to_internal_value('10.5') == 1050

def test_partnerships_list(api_client, create_test_data):
    """
    Тест - выводит заказы
    """
    response = api_client.get("/api/v1/orders")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 2

def test_partnerships_list_sort(api_client, create_test_data):
    """
    Тест - выводит заказы с сортировкой по стране Польша
    """ 
    response = api_client.get("/api/v1/orders?country=Польша")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1


def test_partnerships_get_and_delete(api_client, create_test_data):
    """
    Тест - Удаляет заказы
    """
    response = api_client.get("/api/v1/orders")
    id_1 = response.data["results"][0]["id"]
    id_2 = response.data["results"][1]["id"]

    response = api_client.get(f"/api/v1/orders/{id_1}")
    assert response.status_code == status.HTTP_200_OK

    response = api_client.delete(f"/api/v1/orders/{id_1}")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = api_client.delete(f"/api/v1/orders/{id_2}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    response = api_client.delete(f"/api/v1/orders/{id_1}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_partnerships_created_and_patch(api_client, create_test_data):
    """
    Тест - создает заказы
    """
    response = api_client.get("/api/v1/products")
    assert response.status_code == status.HTTP_200_OK
    product_id_1 = response.data["results"][0]["id"]
    product_id_2 = response.data["results"][1]["id"]

    response = api_client.get("/api/v1/partner")
    assert response.status_code == status.HTTP_200_OK

    person_id_1 = response.data["results"][0]["id"]
    person_id_2 = response.data["results"][1]["id"]

    data_w = dict({"person": person_id_2, "debt_rub": 0})
    response = api_client.post(path="/api/v1/orders", data=data_w, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    data_2 = dict(
        {
            "debt_rub": 2147487,
            "person": person_id_1,
            "supplier": response.data["id"],
            "products": [product_id_1, product_id_2],
        }
    )
    response = api_client.post(path="/api/v1/orders", data=data_2, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    data_3 = dict({"products": [product_id_1]})
    response = api_client.patch(
        path=f"/api/v1/orders/{response.data["id"]}", data=data_3, format="json"
    )
    assert response.status_code == status.HTTP_200_OK


def test_partnerships_error(api_client, create_test_data):
    """
    Тест - создает заказы c ошибками
    1. нет ссылки на поставщика и указана задолжность
    2. нет ссылки на поставщика и есть список поставок
    """
    response = api_client.get("/api/v1/products")
    assert response.status_code == status.HTTP_200_OK
    product_id_1 = response.data["results"][0]["id"]
    product_id_2 = response.data["results"][1]["id"]

    response = api_client.get("/api/v1/partner")
    assert response.status_code == status.HTTP_200_OK

    person_id_1 = response.data["results"][0]["id"]
    person_id_2 = response.data["results"][1]["id"]

    data_w = dict({"person": person_id_2, "debt_rub": 1245.5})
    response = api_client.post(path="/api/v1/orders", data=data_w, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data_w = dict({"person": person_id_2, "products": [product_id_1]})
    response = api_client.post(path="/api/v1/orders", data=data_w, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_partnerships_update_error(api_client, create_test_data):
    """
    Тест - изменяет заказы c ошибками:
    нет ссылки на поставщика и есть список поставок
    """
    response = api_client.get("/api/v1/products")
    assert response.status_code == status.HTTP_200_OK
    product_id_1 = response.data["results"][0]["id"]
    product_id_2 = response.data["results"][1]["id"]

    response = api_client.get("/api/v1/partner")
    assert response.status_code == status.HTTP_200_OK

    person_id_1 = response.data["results"][0]["id"]
    person_id_2 = response.data["results"][1]["id"]

    # Создаем запись без поставщика верхнего уроня
    data_w = dict({"person": person_id_1, "debt_rub": 0})
    response = api_client.post(path="/api/v1/orders", data=data_w, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    # Добавляем поставщику верхнего уроня товары
    data_w = dict({"products": [product_id_1]})
    response = api_client.patch(
        path=f"/api/v1/orders/{response.data['id']}", data=data_w, format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_not_accesse(api_client_not_group, create_test_data):
    """
    Проверка доступа к API пользователя 
    не выходищего в группу 'API_access' 
    """
    response = api_client_not_group.get(
        path=f"/api/v1/orders")
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client_not_group.post(
        path=f"/api/v1/orders", data='{}', format="json"
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client_not_group.delete(
        path=f"/api/v1/orders/1000")
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client_not_group.patch(
        path=f"/api/v1/orders/1000")
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = api_client_not_group.put(
        path=f"/api/v1/orders/1000")
    assert response.status_code == status.HTTP_403_FORBIDDEN
