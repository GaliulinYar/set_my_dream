from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from dream.models import DreamCategory, Dream
from dream.permissions import IsOwner, IsOwnerOrAdmin
from dream.serializers import DreamCategorySerializer, DreamSerializer


class DreamCategoryCreateAPIView(generics.CreateAPIView):
    """Создание категории мечты"""
    permission_classes = [IsAuthenticated | IsAdminUser]
    serializer_class = DreamCategorySerializer


class DreamCategoryListAPIView(generics.ListAPIView):
    """Вывод списка категорий"""
    serializer_class = DreamCategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = DreamCategory.objects.all()


class DreamCategoryRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод деталей категории мечты"""
    serializer_class = DreamCategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = DreamCategory.objects.all()


class DreamCategoryUpdateAPIView(generics.UpdateAPIView):
    """Изменение категории"""
    serializer_class = DreamCategorySerializer
    permission_classes = [IsAuthenticated | IsAdminUser]
    queryset = DreamCategory.objects.all()


class DreamCategoryDestroyAPIView(generics.DestroyAPIView):
    """Удаление категории мечты"""
    permission_classes = [IsAuthenticated | IsAdminUser]
    queryset = DreamCategory.objects.all()


class DreamCreateAPIView(generics.CreateAPIView):
    """Создание мечты"""
    serializer_class = DreamSerializer
    permission_classes = [IsAuthenticated]


class DreamRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод деталей мечты"""
    serializer_class = DreamSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    queryset = Dream.objects.all()


class DreamUpdateAPIView(generics.UpdateAPIView):
    """Изменение мечты"""
    serializer_class = DreamSerializer
    permission_classes = [IsAuthenticated | IsOwner]
    queryset = Dream.objects.all()


class DreamListAPIView(generics.ListAPIView):
    """Вывод списка мечт"""
    serializer_class = DreamSerializer
    permission_classes = [IsAuthenticated | IsOwnerOrAdmin]

    def get_queryset(self):
        # Если пользователь является администратором, возвращаем все объекты
        if self.request.user.is_staff:
            return super().get_queryset()
        # Иначе возвращаем только объекты, принадлежащие текущему пользователю
        return super().get_queryset().filter(user=self.request.user)


class DreamDestroyAPIView(generics.DestroyAPIView):
    """Удаление мечты"""
    queryset = Dream.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]