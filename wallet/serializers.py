from rest_framework import serializers
from wallet.models import Wallet, Transaction, CoinPurchase


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'timestamp', 'description']


class CoinPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinPurchase
        fields = ['amount', 'timestamp']


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    coin_purchases = CoinPurchaseSerializer(many=True, read_only=True)

    class Meta:
        model = Wallet
        fields = ['balance', 'transactions', 'coin_purchases']