from django.db import models

from users.models import User


class Wallet(models.Model):
    """ Модель кошелька пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet', verbose_name='кошелек')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='баланс кошелька')
    coins = models.IntegerField(default=0, verbose_name='монеты')

    def __str__(self):
        return f"Кошелек пользователя {self.user}"


class Transaction(models.Model):
    """Модель трансакций"""
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions', verbose_name='трансакция')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата и время')
    description = models.CharField(max_length=255, verbose_name='назначение')

    def __str__(self):
        return f"Трансакция пользователя {self.wallet.user}, {self.timestamp.strftime('%m-%d-%Y, %H:%M')}, {self.amount}"


class CoinPurchase(models.Model):
    """Модель покупки монет, отражается на балансе кошелька"""
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='coin_purchases', verbose_name='кошелек')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='дата и время')

    def __str__(self):
        return f"{self.wallet.user}, {self.timestamp}, {self.amount}"
