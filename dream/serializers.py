from rest_framework import serializers
from dream.models import DreamCategory, Dream


class DreamCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для создания категории мечты"""

    class Meta:

        model = DreamCategory
        fields = ['id', 'title', 'description', 'image']


class DreamSerializer(serializers.ModelSerializer):
    """Сериализатор для создания мечты"""

    class Meta:

        model = Dream
        fields = ['id', 'title', 'dream_category', 'dream_image', 'cost', 'status']
