# HierarchyBD-Django
python manage.py makemigrations 

python manage.py migrate  
 python manage.py add_user 

  python manage.py runserver

python manage.py loaddata test_data/Counterparties_fixture.json
python manage.py loaddata test_data/Products_fixture.json


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