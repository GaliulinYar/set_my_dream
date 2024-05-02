from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer, UserUpdateSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet для пользователя"""

    serializer_class = UserSerializer  # использованный сериализатор
    queryset = User.objects.all()  # для работы с запросом на Юзера


class UserUpdateView(generics.UpdateAPIView):
    """Представление для редактирования данных пользователя"""

    serializer_class = UserUpdateSerializer  # использованный сериализатор
    permission_classes = [IsAuthenticated]  # подтягиваем авторизованного юзера

    def get_object(self):
        # Извлекаем объект пользователя на основе информации о текущем пользователе
        return self.request.user


