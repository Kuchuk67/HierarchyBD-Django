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
from partnerships.serializer import PartnershipsListSerializer
# Create your views here.
class PartnershipsViewsSet(ViewSet):
    """
    Представление для иерархической сети заказов
    """

    def list(self, request):
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
        pass