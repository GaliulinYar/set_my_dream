from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для создания юзера"""

    class Meta:
        # показываем все поля Юзера
        model = User
        fields = '__all__'  # ['email', 'password', 'first_name', 'id']

    # Шифруем пароль
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        # Устанавливаем зашифрованный пароль
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class UserDocSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения юзера """

    class Meta:
        # показываем нужные поля Юзера
        model = User
        fields = ['email', 'first_name']
