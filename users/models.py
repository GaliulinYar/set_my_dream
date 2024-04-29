from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """Модель юзера"""
    username = None  # для регистрации убираем имя, т.к. меняем его на почту
    email = models.EmailField(max_length=30, unique=True, verbose_name='Почта')  # почта юзера

    USERNAME_FIELD = "email"  # при регистрации меняем поле имя на почту
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
