from rest_framework import permissions

class IsSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user 
            and request.user.is_authenticated
            and request.user.role.name == 'supervisor'
            and request.user.trusted == True
        )