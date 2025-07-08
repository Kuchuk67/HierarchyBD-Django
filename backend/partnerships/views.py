from django.db.models.deletion import RestrictedError
from rest_framework import status
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from partnerships.models import Partnerships
from partnerships.serializer import (
    PartnershipsListSerializer,
    PartnershipsSerializer,
    PartnershipsUpdateSerializer,
)


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

    def destroy(self, request, *args, **kwargs):
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

    def get_serializer_class(self):

        if self.action in ["list", "retrieve"]:
            return PartnershipsListSerializer
        elif self.action in ["update", "partial_update"]:
            return PartnershipsUpdateSerializer
        return PartnershipsSerializer
