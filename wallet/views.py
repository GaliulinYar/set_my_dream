from rest_framework import generics, status
from rest_framework.response import Response
from wallet.models import Wallet, Transaction, CoinPurchase
from wallet.serializers import WalletSerializer, TransactionSerializer, CoinPurchaseSerializer


class WalletCreateAPIView(generics.CreateAPIView):
    serializer_class = WalletSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        wallet = Wallet.objects.filter(user=user).first()
        if wallet:
            error_message = "You already have a wallet"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            wallet = serializer.save(user=user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class WalletListAPIView(generics.ListAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class WalletRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class WalletUpdateAPIView(generics.UpdateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class WalletDestroyAPIView(generics.DestroyAPIView):
    queryset = Wallet.objects.all()


class TransactionCreateAPIView(generics.CreateAPIView):
    serializer_class = TransactionSerializer


class TransactionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionListAPIView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionDestroyAPIView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()


class CoinPurchaseCreateAPIView(generics.CreateAPIView):
    serializer_class = CoinPurchaseSerializer


class CoinPurchaseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CoinPurchaseSerializer
    queryset = CoinPurchase.objects.all()


class CoinPurchaseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CoinPurchaseSerializer
    queryset = CoinPurchase.objects.all()


class CoinPurchaseListAPIView(generics.ListAPIView):
    serializer_class = CoinPurchaseSerializer
    queryset = CoinPurchase.objects.all()


class CoinPurchaseDestroyAPIView(generics.DestroyAPIView):
    queryset = CoinPurchase.objects.all()
