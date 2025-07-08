from rest_framework import serializers


class SupplierValidator:
    """
    Валидатор на проверку нумерации int >= 1
    """

    requires_context = True

    def __init__(self, products: list = [], supplier: int | None = None) -> None:
        self.supplier = supplier
        self.products = products

    def __call__(self, attrs, serializer_field):
        """
        Проверка корректности
        "supplier",
        "products",
        "debt_rub"
        """
        products = (serializer_field.initial_data.get(self.products),)

        if not serializer_field.initial_data.get(self.supplier) and len(products) > 0:
            raise serializers.ValidationError(
                "If there is no supplier - there are no products"
            )
