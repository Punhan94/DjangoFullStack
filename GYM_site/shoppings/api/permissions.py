from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = 'Siz burada deyisiklik ede bilmezsiniz'
    def has_object_permission(self, request, view, obj):
        # return (object.user == request.user) or request.user.is_superuser
        return  request.user.is_superuser