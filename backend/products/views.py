from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from products.models import Products
from products.serializer import ProductsSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasAPIGroupPermission

class ProductsViewsSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    """
    Представление для продукции
    """
    permission_classes = [IsAuthenticated, HasAPIGroupPermission]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
