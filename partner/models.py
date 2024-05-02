import uuid
from django.db import models
from users.models import User


# Create your models here.
class Referral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Привязка к Юзеру
    referral_link = models.UUIDField(default=uuid.uuid4, editable=False,
                                     unique=True)  # UUID будет генерировать уникальную ссылку
    referral_reward = models.DecimalField(max_digits=5, decimal_places=2,
                                          default=0.10)  # Хранит вознаграждение в процентах (10%)
    referral_count = models.IntegerField(default=0)  # кол-во приглашенных по ссылке

    def __str__(self):
        return f"Реферальная ссылка: {self.referral_link}, Вознагрождение в процентах: {self.referral_reward}"
