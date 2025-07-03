from rest_framework.serializers import ModelSerializer
from products.models import Products
# from habit_tracker.task import TaskManager
# from habit_tracker.validators import (    HabitNiceValid)

class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id",
            "name_product",
            "model_product",
            "release_date",
        ]