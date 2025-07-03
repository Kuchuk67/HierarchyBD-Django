from rest_framework.generics import ListAPIView
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from rest_framework.viewsets import ModelViewSet
from products.models import Products
from products.serializer import ProductsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
# from users.permissions import HasAPIGroupPermission


class ProductsViewsSet(ModelViewSet):
    """
    Представление для продукции
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated,] #HasAPIGroupPermission]