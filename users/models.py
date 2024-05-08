from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    """Модель юзера"""
    username = None  # для регистрации убираем имя, т.к. меняем его на почту
    email = models.EmailField(max_length=30, unique=True, verbose_name='Почта')  # почта юзера
    # Добавляем поле для гендера
    GENDER_CHOICES = (
        ('N', 'Не выбран'),
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    # Поле выбора гендера
    gender = models.CharField(max_length=1, default='N', choices=GENDER_CHOICES, verbose_name='Пол', **NULLABLE)

    # Поле для аватара пользователя
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name='Аватар')

    USERNAME_FIELD = "email"  # при регистрации меняем поле имя на почту
    REQUIRED_FIELDS = []

    # мета описание
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    # Текстовое представление
    def __str__(self):
        return self.email

