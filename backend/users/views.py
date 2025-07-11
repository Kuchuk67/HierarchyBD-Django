from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from config.permissions import OwnerPermissionsClass
from users.models import CustomUser
from users.serializer import UserCreateSerializer, UserSerializer
from typing import Any

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [OwnerPermissionsClass | IsAdminUser]

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        print(kwargs, request.user.pk)
        return super().retrieve(request, *args, **kwargs)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()
