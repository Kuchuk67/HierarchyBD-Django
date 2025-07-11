# HierarchyBD-Django
### Описание проекта: «Сеть по продаже электроники»

Разработка веб-приложения с API-интерфейсом и административной панелью для моделирования и управления иерархической сетью по продаже электронной продукции.

## Функциональные возможности
1. #### Модель сети

Приложение моделирует трехуровневую сеть распространения электроники, состоящую из:
* Заводов (уровень 0),

* Розничных сетей (уровень 1 и выше),

* Индивидуальных предпринимателей (уровень 1 и выше).

Каждое звено может иметь только одного поставщика - родителя в  иерархической таблице.

Каждое звено сети включает:
*  Название,
*  Контактную информацию:
*  email,
*  страна,
*  город,
*  улица,
*  номер дома,
*  Продукты (название, модель, дата выхода),
*  Ссылку на поставщика,
*  Задолженность перед поставщиком (decimal с точностью до копеек),
*  Автоматическую отметку времени создания.

2. #### Структура данных
БД состоит из связанных таблиц обеспечивающих каждое звено сети:
* Контрагенты 
* Продукты (товары)
* Контракты (заказы)

Вспомогательная таблица для реализвции доступа
* Пользователи 

## Административная панель Django

* Просмотр и редактирование Контрагентов и Товаров

* Просмотр и редактирование объектов сети.

Вывод всех созданных объектов с возможностью фильтрации по городу.

- Реализован admin action для обнуления задолженности перед поставщиком у выбранных объектов.


## API-интерфейс на базе Django REST Framework
CRUD-операции для Контрагентов.
CRUD-операции для Товаров.
CRUD-операции для Звеньев сети.

Обновление поля «задолженность перед поставщиком» через API не реализовано(запрещено).

Возможность фильтрации по стране.

### Аутентификация: 
доступ к API разрешен только аутотенфицированным  сотрудникам и имеющим группу 'API_access'

# Установка HierarchyBD-Django

## Docker

Проект находится под системой управления и контеризации - **Docker**.
Если у вас нет Docker - вы можете установить его
с официального сайта: [Docker](https://www.docker.com/get-started/)

## Enviroments

Необходимо заполнить в папке backend файл **env_example** и в последствии 
переименовать его в **.env**

## Start
Необходимо ввести команды:
```bash
docker compose up
```


Админка Джанго будет доступена по адресу:
[http://localhost/admin/](http://localhost/admin/)\
API-cервис будет доступен по адресу:
[http://localhost/api/v1/swagger/](http://localhost/api/v1/)\
Документация API
[http://localhost/api/v1/swagger/](http://localhost/api/v1/swagger/)

## Данные для демо-доступа:
При загрузке демо-данных параметры доступа:\
email = "admin@example.com"\
password = "54321"
Создание суперадмина
```
python manage.py add_user 
```

## Демо данные
Установка производится автоматом

Усли демоданные не нужны - убрать строки\
с loaddata и add_user_auto\
из файла docker-compose.yaml


## Testing
Для тестирования нужно перейти внутрь контейнера.

- Найдите контейнер:

```bash
docker ps
```

Ищите контейнер с именем приложения и возьмите
первые 3 символа CONTAITER ID

- Войдите в контейнер:

```bash
docker exec -it YourCONTAINERID bash
```

- Запустите тест

После этого вы попадете внутрь контейнера  
и можете стандартно запускать тесты внутри контейнера

```bash
cd backend
pytest
```

python manage.py makemigrations 

python manage.py migrate  
 python manage.py add_user 

  python manage.py runserver

python manage.py loaddata test_data/Counterparties_fixture.json
python manage.py loaddata test_data/Products_fixture.json
python manage.py loaddata test_data/Partnerships_fixture.json

  python -Xutf8 manage.py dumpdata products.Products --output test_data/Products_fixture.json --indent 4
python -Xutf8 manage.py dumpdata partnerships.Partnerships --output test_data/Partnerships_fixture.json --indent 4
    python -Xutf8 manage.py dumpdata counterparties.Counterparties --output test_data/Counterparties_fixture.json --indent 4





```
select cc.name, cc.that_is_type, ps.*, cc2.name, cc2.that_is_type
from partnerships_partnerships as ps 
join counterparties_counterparties as cc 
on ps.person_id=cc.id 
join partnerships_partnerships as ps2
on ps.supplier_id=ps2.id
join counterparties_counterparties as cc2 
on ps2.person_id=cc2.id 
```