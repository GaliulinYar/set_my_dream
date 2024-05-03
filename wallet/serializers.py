from rest_framework import serializers
from wallet.models import Wallet, Transaction, CoinPurchase


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance', 'coins']
        read_only_fields = ['user']


class TransactionSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format='%m-%d-%Y, %H:%M', read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'wallet', 'amount', 'timestamp', 'description']


class CoinPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinPurchase
        fields = ['id', 'wallet', 'amount', 'timestamp']