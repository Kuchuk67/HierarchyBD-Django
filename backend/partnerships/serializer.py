from rest_framework.serializers import ModelSerializer, SerializerMethodField
from partnerships.models import Partnerships
from counterparties.models import Counterparties


class CounterpartySerializer(ModelSerializer):
    class Meta:
        model = Counterparties
        fields =  [
            "id",
            "name",
            "that_is_type",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "active",
        ]


class PartnershipsListSerializer(ModelSerializer):

    person = CounterpartySerializer(read_only=True)
    supplier = SerializerMethodField()

    def get_supplier(self, obj):
        if obj.supplier:
            return {
                "id": obj.supplier.id,
                "name": obj.supplier.person.name,
                "that_is_type": obj.supplier.person.that_is_type,
                "email": obj.supplier.person.email,
                "country": obj.supplier.person.country,
                "city": obj.supplier.person.city,
                "street": obj.supplier.person.street,
                "house_number": obj.supplier.person.house_number,
                "active": obj.supplier.person.active,
            }
        return None
    
    class Meta:
        model = Partnerships
        fields = [
            "id",
            "debt",
            "data_create",
            "person",
            "supplier",
            #"person_name",
            #"supplier_name"
        ]