from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Разрешение для владельца объекта."""

    def has_object_permission(self, request, view, obj):
        if request.user() == obj.user:
            return True



class IsOwnerOrAdmin(BasePermission):
    """Разрешение для владельца объекта или администратора."""

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли текущий пользователь владельцем объекта
        return obj.user == request.user or request.user.is_staff

    def has_permission(self, request, view):
        # Разрешаем доступ только для аутентифицированных пользователей
        return request.user.is_authenticated