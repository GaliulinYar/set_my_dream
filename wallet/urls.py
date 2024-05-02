# from django.urls import path
# from wallet.views import (WalletListView, WalletDetailView, TransactionCreateView, TransactionListView,
#                           TransactionDetailView, CoinPurchaseListView, CoinPurchaseDetailView, WalletCreateView)
#
#
# app_name = 'wallet'
#
# urlpatterns = [
#     path('', WalletListView.as_view(), name='wallet_list'),
#     path('wallet/<int:pk>/', WalletDetailView.as_view(), name='wallet_detail'),
#     path('wallet/create/', WalletCreateView.as_view(), name='wallet-create'),
#     path('transaction/create', TransactionCreateView.as_view(), name='transaction_create'),
#     path('transaction/list', TransactionListView.as_view(), name='transaction_list'),
#     path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
#     path('coin_purchase/', CoinPurchaseListView.as_view(), name='coin_purchase_list'),
#     path('coin_purchase/<int:pk>/', CoinPurchaseDetailView.as_view(), name='coin_purchase_detail'),
# ]