from decimal import Decimal
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from counterparties.models import Counterparties
from partnerships.models import Partnerships
from products.serializer import ProductsSerializer


class MoneyField(serializers.Field):
    """
    Поле для отображения цены, хранимой в копейках, в рублях.
    """

    def to_representation(self, value: int) -> Decimal:
        # Представление: копейки в рубли
        if value:
            return (Decimal(value) / 100).quantize(Decimal("0.01"))
        return Decimal("0.00")

    def to_internal_value(self, data: str) -> int:
        # При приёме данных, конвертим в копейки
        if data:
            try:
                amount = Decimal(data)
            except (TypeError, ValueError):
                raise serializers.ValidationError("Некорректная цена")
            return int((amount * 100).quantize(Decimal("1")))
        return 0


class CounterpartySerializer(ModelSerializer):
    class Meta:
        model = Counterparties
        fields = [
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

    def get_supplier(self, obj: Partnerships) -> dict | None:
        assert isinstance(obj.person, Counterparties)
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

    debt_rub = MoneyField(source="debt")

    class Meta:
        model = Partnerships
        fields = ["id", "debt_rub", "data_create", "person", "supplier", "products"]


class PartnershipsSerializer(ModelSerializer):
    debt_rub = MoneyField(source="debt")

    class Meta:
        model = Partnerships

        fields = ["id", "debt_rub", "data_create", "person", "supplier", "products"]

    def validate(self, data: dict) -> dict:
        supplier = data.get("supplier")
        products = data.get("products", [])
        debt = data.get("debt")

        # print("+++++",debt, supplier, products)

        if supplier is None and (len(products)) > 0:
            raise serializers.ValidationError(
                {"supplier": "If there is no supplier - no products"}
            )

        if supplier is None and (debt is not None and debt > 0):
            raise serializers.ValidationError(
                {"debt_rub": "If there is no supplier - no debt"}
            )
        return data


class PartnershipsUpdateSerializer(ModelSerializer):

    class Meta:
        model = Partnerships
        fields = ["supplier", "products"]


    def validate(self, data: dict) -> dict:
        # Новое значение supplier (может быть None или не передано)
        new_supplier = data.get("supplier", None)
        if new_supplier is None and self.instance:
            assert isinstance(self.instance, Partnerships)
            new_supplier = self.instance.supplier
        '''new_supplier = data.get(
            "supplier", self.instance.supplier if self.instance else None
        )'''
        # Новое значение products (может быть пустым или не передано)
        '''new_products = data.get(
            "products", self.instance.products.all() if self.instance else []
        )'''
        new_products = data.get("products", None)
        if new_products is None and self.instance:
            assert isinstance(self.instance, Partnerships)
            new_products = list(self.instance.products.all()) 

        if new_products:
            if new_supplier is None and len(new_products) > 0:
                raise serializers.ValidationError(
                    {"supplier": "If there is no supplier - no products"}
                )   
        return data
