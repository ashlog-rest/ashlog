from rest_framework.permissions import BasePermission


class IsMemberOrReadOnly(BasePermission):
    """ Allow user to edit the project """

    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to edit their project """

        return request.user in obj.users.all()
