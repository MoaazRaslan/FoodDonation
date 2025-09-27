from rest_framework import permissions

class IsSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user 
            and request.user.is_authenticated
            and request.user.role.name == 'supervisor'
            and request.user.trusted == True
        )
    
class IsRestaurant(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user 
            and request.user.is_authenticated
            and request.user.role.name == 'restaurant'
            and request.user.trusted == True
        )

class IsEvaluator(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user 
            and request.user.is_authenticated
            and request.user.role.name == 'evaluator'
            and request.user.trusted == True
        )
    