from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOrReadyOnly(BasePermission):
    """ Allow user to edit the organization """

    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to edit their organization """
        if request.method in SAFE_METHODS:
            return True

        return request.user in obj.members.all()
