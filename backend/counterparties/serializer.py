from rest_framework.serializers import ModelSerializer
from counterparties.models import Counterparties
# from habit_tracker.task import TaskManager
# from habit_tracker.validators import (    HabitNiceValid)

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