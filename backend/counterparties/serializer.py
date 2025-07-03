from rest_framework.serializers import ModelSerializer
from counterparties.models import Counterparties


class CounterpartiesSerializer(ModelSerializer):
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