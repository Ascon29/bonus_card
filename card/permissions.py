from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """ Проверка на суперпользователя. """
    def has_permission(self, request, view):
        return request.user.is_superuser


# class IsOwner(BasePermission):
#     """ Проверка на владельца карты. """
#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user
