from django.db.models.deletion import RestrictedError
from rest_framework import status
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.request import  Request
from rest_framework.viewsets import GenericViewSet

from counterparties.models import Counterparties
from partnerships.models import Partnerships
from partnerships.serializer import (
    PartnershipsListSerializer,
    PartnershipsSerializer,
    PartnershipsUpdateSerializer,
)
from typing import Any
from typing import Type
from rest_framework.serializers import BaseSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasAPIGroupPermission

class PartnershipsViewsSet(
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """
    Представление для продукции
    """
    permission_classes = [IsAuthenticated, HasAPIGroupPermission]

    class CountryFilter(django_filters.FilterSet):
        country = django_filters.CharFilter(field_name='person__country', lookup_expr='icontains')

        class Meta:
            model = Partnerships
            fields = ['country']


    def destroy(self, request:  Request, *args: Any, **kwargs: Any) -> Response:
        """
        Обработка ошибки удавения связанной записи
        или удаляем запись
        """
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except RestrictedError:
            return Response(
                {
                    "error": (
                        "The object cannot be deleted "
                        "because other records is linked to it."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    queryset = Partnerships.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter

    '''def list(self, request, *args, **kwargs):
        self.get_queryset = Partnerships.objects.filter(person__city="Минск")
        #return super().list(request, *args, **kwargs)

        queryset = self.filter_queryset(self.get_queryset())
        print("+++++++++",self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)'''

    def get_serializer_class(self) -> Type[BaseSerializer]:

        if self.action in ["list", "retrieve"]:
            return PartnershipsListSerializer
        elif self.action in ["update", "partial_update"]:
            return PartnershipsUpdateSerializer
        return PartnershipsSerializer
