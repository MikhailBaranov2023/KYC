from rest_framework.permissions import BasePermission


class IsStaffPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff:
            return False
        if not request.method in ['PATCH', 'PUT', 'DELETE', 'POST', 'GET']:
            return False
        return True