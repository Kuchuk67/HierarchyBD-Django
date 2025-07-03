from rest_framework.generics import ListAPIView
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from rest_framework.viewsets import ModelViewSet
from counterparties.models import Counterparties
from counterparties.serializer import CounterpartiesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
from users.permissions import HasAPIGroupPermission


class CounterpartiesViewsSet(ModelViewSet):
    """
    Представление для контрагентов
    """
    #permission_required = "counterparties.API_access"
    # pagination_class = EducationPagination
    queryset = Counterparties.objects.all()
    serializer_class = CounterpartiesSerializer
    permission_classes = [IsAuthenticated, HasAPIGroupPermission]


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

    def list(self, request, *args, **kwargs):
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

    @action(detail=False)
    def all(self, request):
        """
        Дополнительный list
        При выводе списка отображаем и неактивных контрагентов
        """
        parties = Counterparties.objects.all().order_by('name')

        page = self.paginate_queryset(parties)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(parties, many=True)
        return Response(serializer.data)

