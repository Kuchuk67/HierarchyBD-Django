from rest_framework.serializers import ModelSerializer, SerializerMethodField
from partnerships.models import Partnerships
from counterparties.models import Counterparties
from products.serializer import ProductsSerializer
from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
# class ProductSerializer
from decimal import Decimal
#from validators import SupplierValidator
from partnerships import validators


class MoneyField(serializers.Field):
    """
    Поле для отображения цены, хранимой в копейках, в рублях.
    """

    def to_representation(self, value):
        # Представление: копейки → рубли (Decimal for precision)
        return (Decimal(value) / 100).quantize(Decimal('0.01'))

    def to_internal_value(self, data):
        # При приёме данных (если поддерживаете запись)
        # ожидаем рубли, конвертим в копейки
        try:
            amount = Decimal(data)
        except (TypeError, ValueError):
            raise serializers.ValidationError("Некорректная цена")
        return int((amount * 100).quantize(Decimal('1')))  
    

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
    
    debt_rub = MoneyField(source='debt')

    class Meta:
        model = Partnerships
        fields = [
            "id",
            "debt_rub",
            "data_create",
            "person",
            "supplier",
            "products"
         ]
        

class PartnershipsSerializer(ModelSerializer):
    debt_rub = MoneyField(source='debt')
    
    class Meta:
        model = Partnerships
        
        fields = [
            "id",
            "debt_rub",
            "data_create",
            "person",
            "supplier",
            "products"
         ]
    
    def validate(self, data):
        supplier = data.get("supplier")
        products = data.get("products", [])
        debt = data.get("debt_rub")

        if supplier is None and (len(products)) > 0:
            raise serializers.ValidationError({
                "supplier": "Укажите поставщика, если задан продукт."
            })

        if supplier is None and (not debt  or debt > 0):
            raise serializers.ValidationError({
                "debt_rub": "If there is no supplier - no debt"
            })
        return data
    '''def validate_debt_rub(self, value):  
        """
        если нет поставщика - нет продуктов
        """
        if not self.initial_data["supplier"] and self.initial_data["debt_rub"]>0:  
            raise serializers.ValidationError("If there is no supplier - no debt")  
        return value  '''
    

class PartnershipsUpdateSerializer(ModelSerializer):

    class Meta:
        model = Partnerships
        fields = [
            "supplier",
            "products"
         ]
    def validate(self, data):
        # Новое значение supplier (может быть None или не передано)
        new_supplier = data.get("supplier", self.instance.supplier if self.instance else None)
        # Новое значение products (может быть пустым или не передано)
        new_products = data.get("products", self.instance.products.all() if self.instance else [])
        print("******", new_supplier, new_products)

        if new_supplier is None and len(new_products) > 0:
            raise serializers.ValidationError({
                "supplier": "Укажите поставщика, если задан продукт."
            })
        return data
    
