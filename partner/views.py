from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from partner.models import Referral
from partner.serializers import ReferralUrlSerializer


# Create your views here.
class ReferralUrlAPIView(generics.RetrieveAPIView):
    """Вьюшка на просмотр реферальной ссылки"""
    serializer_class = ReferralUrlSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Получаем авторизованного пользователя
        user = self.request.user

        # Получаем объект Referral, связанный с пользователем
        referral = Referral.objects.get(user=user)

        return referral
