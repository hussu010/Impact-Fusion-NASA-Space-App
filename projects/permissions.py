from rest_framework import permissions

class ViewAnyOrIsAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow any users to view project details
    and only authenticated users to update and destroy the projects.
    """

    def has_permission(self, request, view):
        # Allow any request for viewing project details
        if request.method in permissions.SAFE_METHODS:
            return True
        # For other requests, check if the user is authenticated
        return request.user and request.user.is_authenticated
