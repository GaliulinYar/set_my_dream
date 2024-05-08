from partner.views import ReferralUrlAPIView
from django.urls import path

app_name = 'partner'

urlpatterns = [
    # path('', WalletListAPIView.as_view(), name='wallet_list'),
    path('', ReferralUrlAPIView.as_view(), name='partner'),  # эндпоин на получение реф ссылки
    ]
