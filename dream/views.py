from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from dream.models import DreamCategory, Dream
from dream.serializers import DreamCategorySerializer, DreamSerializer


class DreamCategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = DreamCategorySerializer


class DreamCategoryListAPIView(generics.ListAPIView):
    serializer_class = DreamCategorySerializer
    queryset = DreamCategory.objects.all()


class DreamCategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DreamCategorySerializer
    queryset = DreamCategory.objects.all()


class DreamCategoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = DreamCategorySerializer
    queryset = DreamCategory.objects.all()


class DreamCategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = DreamCategory.objects.all()

class DreamCreateAPIView(generics.CreateAPIView):
    serializer_class = DreamSerializer


class DreamRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DreamSerializer
    queryset = Dream.objects.all()


class DreamUpdateAPIView(generics.UpdateAPIView):
    serializer_class = DreamSerializer
    queryset = Dream.objects.all()


class DreamListAPIView(generics.ListAPIView):
    serializer_class = DreamSerializer
    queryset = Dream.objects.all()


class DreamDestroyAPIView(generics.DestroyAPIView):
    queryset = Dream.objects.all()