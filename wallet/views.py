from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from wallet.models import Wallet, Transaction, CoinPurchase
from wallet.permissions import IsOwner, IsOwnerOrAdmin
from wallet.serializers import WalletSerializer, TransactionSerializer, CoinPurchaseSerializer


class WalletCreateAPIView(generics.CreateAPIView):
    """Контроллер создания кошелька пользователя"""
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        wallet = Wallet.objects.filter(user=user).first()
        # Проверяем, если кошелек уже есть у пользователя
        if wallet:
            error_message = "You already have a wallet"
            # если есть, выдаем сообщение об ошибке
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # если кошелька нет, создаем его
            wallet = serializer.save(user=user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class WalletListAPIView(generics.ListAPIView):
    """ Вывод списка кошельков."""
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]
    queryset = Wallet.objects.all()


class WalletRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр кошелька."""
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    queryset = Wallet.objects.all()


# class WalletUpdateAPIView(generics.UpdateAPIView):
#     """ Изменение кошелька."""
#     serializer_class = WalletSerializer
#     permission_classes = [IsAuthenticated | IsOwner]
#     queryset = Wallet.objects.all()


class WalletDestroyAPIView(generics.DestroyAPIView):
    """ Удаление кошелька."""
    permission_classes = [IsAuthenticated | IsOwner]
    queryset = Wallet.objects.all()


class TransactionCreateAPIView(generics.CreateAPIView):
    """ Создание трансакции."""
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer


class TransactionRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод деталей трансакции."""
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    queryset = Transaction.objects.all()


# class TransactionUpdateAPIView(generics.UpdateAPIView):
#     """ Изменение трансакции."""
#     serializer_class = TransactionSerializer
#     permission_classes = [IsAuthenticated | IsOwner]
#     queryset = Transaction.objects.all()


class TransactionListAPIView(generics.ListAPIView):
    """ Вывод списка трансакций."""
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated | IsOwnerOrAdmin]

    def get_queryset(self):
        # Если пользователь является администратором, возвращаем все объекты
        if self.request.user.is_staff:
            return super().get_queryset()
        # Иначе возвращаем только объекты, принадлежащие текущему пользователю
        return super().get_queryset().filter(user=self.request.user)


class TransactionDestroyAPIView(generics.DestroyAPIView):
    """ Удаление трансакции."""
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class CoinPurchaseCreateAPIView(generics.CreateAPIView):
    """ Создание покупки монет."""
    serializer_class = CoinPurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Увеличиваем количество монет в кошельке после создания покупки."""
        coin_purchase = serializer.save(wallet=self.request.user.wallet)
        wallet = coin_purchase.wallet
        wallet.coins += self.get_coins_from_amount(coin_purchase.amount)
        wallet.save()

    def get_coins_from_amount(self, amount):
        """ Преобразование суммы покупки в количество монет."""

        return int(amount)


class CoinPurchaseRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод деталей покупки монет."""
    serializer_class = CoinPurchaseSerializer
    permission_classes = [IsAuthenticated | IsOwnerOrAdmin]
    queryset = CoinPurchase.objects.all()


class CoinPurchaseUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование покупки монет."""
    serializer_class = CoinPurchaseSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    queryset = CoinPurchase.objects.all()


class CoinPurchaseListAPIView(generics.ListAPIView):
    """ Вывод списка покупок монет."""
    serializer_class = CoinPurchaseSerializer
    permission_classes = [IsAuthenticated | IsOwnerOrAdmin]

    def get_queryset(self):
        # Если пользователь является администратором, возвращаем все объекты
        if self.request.user.is_staff:
            return super().get_queryset()
        # Иначе возвращаем только объекты, принадлежащие текущему пользователю
        return super().get_queryset().filter(user=self.request.user)

# class CoinPurchaseDestroyAPIView(generics.DestroyAPIView):
#     """ Удаление покупки монет."""
#     queryset = CoinPurchase.objects.all()
#     permission_classes = [IsAuthenticated | IsOwner]
