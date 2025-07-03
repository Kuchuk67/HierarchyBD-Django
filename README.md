# HierarchyBD-Django
python manage.py makemigrations 

python manage.py migrate  
 python manage.py add_user 

  python manage.py runserver

python manage.py loaddata test_data/Counterparties_fixture.json
python manage.py loaddata test_data/Products_fixture.json


  python -Xutf8 manage.py dumpdata products.Products --output test_data/Products_fixture.json --indent 4

    python -Xutf8 manage.py dumpdata counterparties.Counterparties --output test_data/Counterparties_fixture.json --indent 4