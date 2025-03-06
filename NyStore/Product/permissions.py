from rest_framework.permissions import BasePermission, SAFE_METHODS

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to create, update, or delete products.
    Others can only view (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # Allow GET, HEAD, OPTIONS for everyone
            return True
        return request.user and request.user.is_staff