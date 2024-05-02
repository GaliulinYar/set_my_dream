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

    # Обрезаем автар и делаем его 300х300
    # def save(self, *args, **kwargs):
    #     # Проверяем, есть ли загруженный аватар
    #     if self.avatar:
    #         # Открываем изображение
    #         img = Image.open(self.avatar)
    #         # Получаем размеры изображения
    #         width, height = img.size
    #         # Находим минимальный размер
    #         min_size = min(width, height)
    #         # Определяем координаты для обрезки (левая верхняя, правая нижняя)
    #         left = (width - min_size) / 2
    #         top = (height - min_size) / 2
    #         right = (width + min_size) / 2
    #         bottom = (height + min_size) / 2
    #         # Обрезаем изображение до квадрата
    #         img = img.crop((left, top, right, bottom))
    #         # Масштабируем изображение до 300x300 пикселей
    #         img.thumbnail((300, 300), Image.ANTIALIAS)
    #         # Сохраняем обработанное изображение
    #         img.save(self.avatar.path)
    #     super().save(*args, **kwargs)
