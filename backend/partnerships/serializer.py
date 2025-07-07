from rest_framework.serializers import ModelSerializer, SerializerMethodField
from partnerships.models import Partnerships
from counterparties.models import Counterparties
from products.serializer import ProductsSerializer
from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
# class ProductSerializer


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

    products = ProductsSerializer(many=True, read_only=True)

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
            "products"
         ]
        

class PartnershipsSerializer(ModelSerializer):

    class Meta:
        model = Partnerships
        fields = [
            "id",
            "debt",
            "data_create",
            "person",
            "supplier",
            "products"
         ]
        

class PartnershipsUpdateSerializer(ModelSerializer):

    class Meta:
        model = Partnerships
        fields = [
            "supplier",
            "products"
         ]
