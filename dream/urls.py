from django.urls import path
from dream.views import (DreamCategoryCreateAPIView, DreamCategoryListAPIView, DreamCategoryRetrieveAPIView,
                         DreamCategoryUpdateAPIView, DreamCreateAPIView, DreamListAPIView, DreamRetrieveAPIView,
                         DreamUpdateAPIView, DreamCategoryDestroyAPIView, DreamDestroyAPIView)


app_name = 'dream'

urlpatterns = [
    path('dream_category/create/', DreamCategoryCreateAPIView.as_view(), name='dream_category_create'),
    path('dream_category/', DreamCategoryListAPIView.as_view(), name='dream_category_list'),
    path('dream_category/<int:pk>/', DreamCategoryRetrieveAPIView.as_view(), name='dream_category_detail'),
    path('dream_category/update/<int:pk>/', DreamCategoryUpdateAPIView.as_view(), name='dream_category_update'),
    path('dream_category/delete/<int:pk>/', DreamCategoryDestroyAPIView.as_view(), name='dream_category_delete'),
    path('dream/create/', DreamCreateAPIView.as_view(), name='dream_create'),
    path('dream/', DreamListAPIView.as_view(), name='dream_list'),
    path('dream/<int:pk>/', DreamRetrieveAPIView.as_view(), name='dream_detail'),
    path('dream/update/<int:pk>/', DreamUpdateAPIView.as_view(), name='dream_update'),
    path('dream/delete/<int:pk>/', DreamDestroyAPIView.as_view(), name='dream_delete')
]
