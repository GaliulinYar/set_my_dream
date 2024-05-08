from partner.models import Referral
from rest_framework import serializers


class ReferralUrlSerializer(serializers.ModelSerializer):
    """Сериализатор для действий с реферальной ссылкой"""

    class Meta:
        model = Referral
        fields = ['referral_link']
