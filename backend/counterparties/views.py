from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from counterparties.models import Counterparties
from counterparties.serializer import CounterpartiesSerializer
from rest_framework.request import Request
from typing import Any

class CounterpartiesViewsSet(ModelViewSet):
    """
    Представление для контрагентов
    """

    queryset = Counterparties.objects.all()
    serializer_class = CounterpartiesSerializer

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Не будем удалять запись, помечаем не активной
        """
        instance = self.get_object()
        if not instance:
            return Response(
                {"error": "Not found the Counterparties"},
                status=status.HTTP_404_NOT_FOUND,
            )
        instance.active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request: Request, deactive: bool=False, *args: Any, **kwargs: Any) -> Response:
        """
        При выводе списка отображаем только активных контрагентов
        """
        parties = Counterparties.objects.filter(active=True).order_by("name")

        page = self.paginate_queryset(parties)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(parties, many=True)
        return Response(serializer.data)

    # Декоратор для отображения Swagger параметров пагинации
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="limit",
                type=int,
                location=OpenApiParameter.QUERY,
                description="Limit items",
            ),
            OpenApiParameter(
                name="offset",
                type=int,
                location=OpenApiParameter.QUERY,
                description="Offset",
            ),
        ],
        responses=CounterpartiesSerializer(many=True),
    )
    @action(detail=False, methods=["get"], url_path="deactive")
    def deactive(self, request: Request) -> Response:
        """
        Выводит список не активных (удаленных) контрагентов
        """
        queryset = self.get_queryset().filter(active=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
