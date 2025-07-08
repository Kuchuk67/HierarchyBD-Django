from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from products.models import Products
from products.serializer import ProductsSerializer


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

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
