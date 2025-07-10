from rest_framework.permissions import BasePermission
from typing import Any


class HasAPIGroupPermission(BasePermission):
    def has_permission(self, request: Any, view: Any) -> Any:
        return request.user and request.user.groups.filter(name="API_access").exists()
