from django.shortcuts import render
from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet для пользователя"""

    serializer_class = UserSerializer  # использованный сериализатор
    queryset = User.objects.all()  # для работы с запросом на Юзера
