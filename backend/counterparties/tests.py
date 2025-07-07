from rest_framework import status


def test_counterparties_created(api_client, 
                                create_test_data
                                ):
    """
    Тест - выводит только активных контрагантов
    """
    response = api_client.get("/api/v1/partner")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 2


def test_counterparties_created_all(
        api_client, 
        create_test_data
        ):
    """
    Тест - выводит только удаленных контрагантов
    """
    response = api_client.get("/api/v1/partner/deactive")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1


def test_counterparties_post(
        api_client, 
        create_test_data, 
        counterparties_post
        ):
    response = api_client.post(path="/api/v1/partner",
                               data=counterparties_post,
                               format="json"
                               )
    assert response.status_code == status.HTTP_201_CREATED

    response = api_client.get("/api/v1/partner")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 3


def test_counterparties_put(
        api_client, 
        create_test_data, 
        counterparties_post, 
        counterparties_put
        ):
    response = api_client.post(path="/api/v1/partner",
                               data=counterparties_post,
                               format="json"
                               )
    assert response.status_code == status.HTTP_201_CREATED
    id_product = response.data["id"]
    response = api_client.put(
            path=f"/api/v1/partner/{id_product}",
            data=counterparties_put,
            format="json"
        )
    assert response.status_code == status.HTTP_200_OK


def test_counterparties_patch(
        api_client, 
        create_test_data, 
        counterparties_post, 
        counterparties_put
        ):
    response = api_client.post(path="/api/v1/partner",
                               data=counterparties_post,
                               format="json"
                               )
    assert response.status_code == status.HTTP_201_CREATED
    id_product = response.data["id"]
    response = api_client.patch(
            path=f"/api/v1/partner/{id_product}",
            data={"country": "Великобритания"},
            format="json"
        )
    assert response.status_code == status.HTTP_200_OK


def test_counterparties_del_or_get(
        api_client, 
        create_test_data, 
        counterparties_post, 
        counterparties_put
        ):
    response = api_client.post(path="/api/v1/partner",
                               data=counterparties_post,
                               format="json"
                               )
    assert response.status_code == status.HTTP_201_CREATED
    id_product = response.data["id"]
    response = api_client.delete(
            path=f"/api/v1/partner/{id_product}"
        )
    assert response.status_code == status.HTTP_200_OK

    response = api_client.get(
            path=f"/api/v1/partner/{id_product}"
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["active"] == False
