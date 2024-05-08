import uuid

from rest_framework import serializers

from partner.models import Referral
from partner.serializers import ReferralUrlSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания юзера"""

    referral_link = serializers.CharField(source='referral.referral_link', read_only=True)

    class Meta:
        # показываем все поля Юзера
        model = User
        fields = ['email', 'password', 'first_name', 'id', 'referral_link']  # '__all__'

    # Шифруем пароль
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        # Устанавливаем зашифрованный пароль
        if password:
            instance.set_password(password)

        instance.save()

        # Создаем реферальную ссылку для пользователя
        referral_link = uuid.uuid4()
        Referral.objects.create(user=instance, referral_link=referral_link)

        return instance


class UserDocSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения юзера """

    referral_link = ReferralUrlSerializer(source='referral', read_only=True)

    class Meta:
        # показываем нужные поля Юзера
        model = User
        fields = ['email', 'first_name', 'referral_link']


class UserUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления данных пользователя в ЛК кабинете юзера"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'avatar')  # Поля для сериализатора

