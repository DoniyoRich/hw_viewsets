from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Проверка пользователя на принадлежность к группе модераторов.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderator").exists()


class IsOwner(permissions.BasePermission):
    """
    Проверка объекта на принедлежность пользователю.
    """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
