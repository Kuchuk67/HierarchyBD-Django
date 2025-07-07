import pytest
from rest_framework.test import APIClient
from users.models import CustomUser
from products.models import Products
from counterparties.models import Counterparties
from partnerships.models import Partnerships

@pytest.fixture
def admin_user(db):
    user = CustomUser.objects.create(
        email="user@user.com",
        is_staff=True,
        is_superuser=True,
    )
    user.set_password("123456789")
    user.save()

    return user

@pytest.fixture
def api_client(admin_user):
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client

@pytest.fixture
def create_test_data(api_client):
    """
    Заполняем началиные данные в БД
    """
    product_1 = Products.objects.create(
        name_product="Продукт 1",
        model_product="Модель продукта 1",
        release_date="2025-07-07"
    )
    product_2 = Products.objects.create(
        name_product="Продукт 1",
        model_product="Модель продукта 1",
        release_date="2025-07-07"
    )
    partner_1 = Counterparties.objects.create(
        name="Smart Factory S.A.",
        that_is_type="factory",
        email="contact@smartfactory.pl",
        country="Польша",
        city="Варшава",
        street="Nowy Świat",
        house_number=12,
        active=True,
    )
    partner_2 = Counterparties.objects.create(
        name="Рога и копыта",
        that_is_type="PE",
        email="4535@fg.pl",
        country="dfdf",
        city="Варшdfdfава",
        street="ffff",
        house_number=12,
        active=False
    )
    partner_3 = Counterparties.objects.create(
        name="Smadddactory S.A.",
        that_is_type="PE",
        email="codddct@smartfactory.pl",
        country="Польша",
        city="Варшава",
        street="Nowy Świat",
        house_number=12,
        active=True,
    )
    
    partnerships_1 = Partnerships.objects.create(
        person=partner_1,
    )
    
    partnerships_2 = Partnerships.objects.create(
        person=partner_2,
        supplier=partnerships_1,
        debt=15012000,
    )
    partnerships_2.products.set([product_1, product_2])


    

@pytest.fixture
def product_one():
    return dict({
        "name_product": "Продукт 2",
        "model_product": "Модель продукта 2",
        "release_date": "2024-07-07"
    })

@pytest.fixture
def product_patch():
    return dict({
        'name_product': 'Продукт изменен'
    })

@pytest.fixture
def product_put():
    return dict({
        "name_product": "Продукт 11",
        "model_product": "Модель продукта 11",
        "release_date": "2025-07-07"
    })


@pytest.fixture
def counterparties_post():
    return dict({
        "name": "ЗАО РитейлМаркет",
        "that_is_type": "retail",
        "email": "info@retailmarket.ru",
        "country": "Россия",
        "city": "Санкт-Петербург",
        "street": "Невский проспект",
        "house_number": "21",
        "active": True
    })

@pytest.fixture
def counterparties_put():
    return dict({
        "name": "ИП Иванов Петр",
        "that_is_type": "PE",
        "email": "ivanovp@pemail.ru",
        "country": "Россия",
        "city": "Казань",
        "street": "Баумана",
        "house_number": "5",
        "active": True
    })
