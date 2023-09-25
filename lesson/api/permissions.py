from rest_framework import permissions

class IsUserAllowedToAccessProduct(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or obj.users_with_access.filter(id=request.user.id).exists()