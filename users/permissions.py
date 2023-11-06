from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return False


class IsStaffPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.id:
            return True
        return False
