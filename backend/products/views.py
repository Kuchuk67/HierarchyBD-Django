from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import status

# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListAPIView

# from users.permissions import HasAPIGroupPermission
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

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
