from rest_framework.permissions import BasePermission

class HasAPIGroupPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="API_access").exists()