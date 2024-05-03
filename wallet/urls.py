from django.urls import path
from wallet.views import (WalletListAPIView, WalletCreateAPIView,  WalletDestroyAPIView, WalletRetrieveAPIView,
                          TransactionListAPIView, TransactionCreateAPIView, TransactionDestroyAPIView,
                          TransactionRetrieveAPIView, CoinPurchaseRetrieveAPIView,
                          CoinPurchaseListAPIView, CoinPurchaseCreateAPIView, CoinPurchaseUpdateAPIView)
# CoinPurchaseDestroyAPIView, WalletUpdateAPIView, TransactionUpdateAPIView
app_name = 'wallet'

urlpatterns = [
    path('', WalletListAPIView.as_view(), name='wallet_list'),
    path('wallet/<int:pk>/', WalletRetrieveAPIView.as_view(), name='wallet_detail'),
    path('wallet/create/', WalletCreateAPIView.as_view(), name='wallet_create'),
    #path('wallet/update/<int:pk>/', WalletUpdateAPIView.as_view(), name="wallet_update"),
    path('wallet/delete/<int:pk>/', WalletDestroyAPIView.as_view(), name="wallet_delete"),
    path('transaction/create', TransactionCreateAPIView.as_view(), name='transaction_create'),
    path('transaction/', TransactionListAPIView.as_view(), name='transaction_list'),
    path('transaction/<int:pk>/', TransactionRetrieveAPIView.as_view(), name='transaction_detail'),
    #path('transaction/update/<int:pk>/', TransactionUpdateAPIView.as_view(), name="transaction_update"),
    path('transaction/delete/<int:pk>/', TransactionDestroyAPIView.as_view(), name="transaction_delete"),
    path('coin_purchase/create/', CoinPurchaseCreateAPIView.as_view(), name='transaction_create'),
    path('coin_purchase/', CoinPurchaseListAPIView.as_view(), name='coin_purchase_list'),
    path('coin_purchase/<int:pk>/', CoinPurchaseRetrieveAPIView.as_view(), name='coin_purchase_detail'),
    path('coin_purchase/update/<int:pk>/', CoinPurchaseUpdateAPIView.as_view(), name='coin_purchase_update'),
    # path('coin_purchase/delete/<int:pk>/', CoinPurchaseDestroyAPIView.as_view(), name='coin_purchase_delete'),
]