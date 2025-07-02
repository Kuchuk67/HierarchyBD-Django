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



