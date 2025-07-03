from rest_framework.generics import ListAPIView
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
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


class CounterpartiesViewsSet(ModelViewSet):
    """
    Представление для контрагентов
    """
    #permission_required = "counterparties.API_access"
    # pagination_class = EducationPagination
    queryset = Counterparties.objects.all()
    serializer_class = CounterpartiesSerializer
    #permission_classes = [IsAuthenticated, HasAPIGroupPermission]
    


    def destroy(self, request, *args, **kwargs):
        """
        Не будем удалять запись, помечаем не активной 
        """
        instance = self.get_object()
        if not instance:
            return Response({'error': 'Not found the Counterparties'}, status=status.HTTP_404_NOT_FOUND)

        instance.active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, deactive = False, *args, **kwargs):
        """
        При выводе списка отображаем только активных контрагентов
        """
        parties = Counterparties.objects.filter(active=True).order_by('name')

        page = self.paginate_queryset(parties)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(parties, many=True)
        return Response(serializer.data)
    
    # Декоратор для отображения Swagger параметров пагинации
    @extend_schema(
        parameters=[
            OpenApiParameter(name='limit', type=int, location=OpenApiParameter.QUERY, description='Limit items'),
            OpenApiParameter(name='offset', type=int, location=OpenApiParameter.QUERY, description='Offset'),
        ],
        responses=CounterpartiesSerializer(many=True),
    )
    @action(detail=False, methods=["get"], url_path="deactive")
    def deactive(self, request):
        queryset = self.get_queryset().filter(active=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




