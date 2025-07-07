from rest_framework.viewsets import ModelViewSet, ViewSet
from counterparties.models import Counterparties
from counterparties.serializer import CounterpartiesSerializer
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from partnerships.models import Partnerships
from partnerships.serializer import(
    PartnershipsListSerializer, 
    PartnershipsSerializer, 
    PartnershipsUpdateSerializer
    )
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin, 
    CreateModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
    )
from rest_framework.pagination import PageNumberPagination
from django.db.models.deletion import RestrictedError


class PartnershipsViewsSet(
    ListModelMixin, 
    CreateModelMixin, 
    UpdateModelMixin, 
    RetrieveModelMixin, 
    DestroyModelMixin, 
    GenericViewSet
    ):
    """
    Представление для продукции
    """
    def destroy(self, request, *args, **kwargs):
        """
        Обработка ошибки удавения связанной записи
        или удаляем запись
        """
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except RestrictedError as e:
            return Response(
                {"error": "The object cannot be deleted because other records is linked to it."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    queryset = Partnerships.objects.all()


    def get_serializer_class(self):
        
        if self.action in ['list', 'retrieve']:
            return PartnershipsListSerializer
        elif self.action in ['update', 'partial_update']:
            return PartnershipsUpdateSerializer
        return PartnershipsSerializer
    