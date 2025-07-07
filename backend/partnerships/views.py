from rest_framework.viewsets import ModelViewSet, ViewSet
from counterparties.models import Counterparties
from counterparties.serializer import CounterpartiesSerializer
#from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
#from users.permissions import HasAPIGroupPermission
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



# Create your views here.


class PartnershipsViewsSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, 
                           GenericViewSet):
    """
    Представление для продукции
    """
    queryset = Partnerships.objects.all()
    #serializer_class = PartnershipsListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PartnershipsListSerializer
        elif self.action == 'retrieve':
            return PartnershipsSerializer
        elif self.action == 'create':
            return PartnershipsSerializer
        elif self.action in ['update', 'partial_update']:
            return PartnershipsUpdateSerializer
        return PartnershipsSerializer
    
'''    def list(self, request, *args, **kwargs):
        # Кастомная логика для списка
        queryset = Partnerships.objects.all()
        serializer = PartnershipsListSerializer(queryset, many=True, context=self.get_serializer_context())
        return super().list(request, *args, **kwargs)
    
    
    def update(self, request, *args, **kwargs):
        queryset = Partnerships.objects.all()
        serializer = PartnershipsUpdateSerializer(queryset, many=True, context=self.get_serializer_context())
        return super().update(request, *args, **kwargs)'''

# class PartnershipsViewsSet(ListModelMixin, GenericViewSet):
"""
    Представление для иерархической сети заказов
    """


''' def list(self, request) -> Response:
        queryset = Partnerships.objects.all()
        serializer = PartnershipsListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass'''