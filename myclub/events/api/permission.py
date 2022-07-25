from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsEventManager(BasePermission):
    message='You are NOT the Event Manager'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.manager==request.user


class IsVenueOwner(BasePermission):
    message='You are NOT the Venue Owner'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.owner==request.user