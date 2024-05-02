from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UserConfig
from users.views import UserViewSet, UserUpdateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Добавили связи с Юзером
app_name = UserConfig.name

# роутер viewset users
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # паттерны для авторизации
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # получение токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # сброс токена на другой

    path('users/update/', UserUpdateView.as_view(), name='user-update'),  # редактирование данных юзера для ЛК

] + router.urls
