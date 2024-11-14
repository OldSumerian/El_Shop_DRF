from typing import List

from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from el_shop.models import NetElement
from el_shop.serializers import NetElementCreateSerializer, NetElementListSerializer, NetElementSerializer


class NetElementCreateView(CreateAPIView):
    """
    Создание элемента сети
    """
    model: models.Model = NetElement
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: serializers.ModelSerializer = NetElementCreateSerializer


class NetElementListView(ListAPIView):
    """
    Получение списка всех элементов сети
    """
    model: models.Model = NetElement
    queryset: List[NetElement] = NetElement.objects.all()
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: serializers.ModelSerializer = NetElementListSerializer
    filter_backends: list = [DjangoFilterBackend,]
    filterset_fields: List[str] = ["contact__country", ]


class NetElementView(RetrieveUpdateDestroyAPIView):
    """
    Получение, редактирование и удаление элемента сети
    """
    model: models.Model = NetElement
    queryset: List[NetElement] = NetElement.objects.all()
    serializer_class: serializers.ModelSerializer = NetElementSerializer
    permission_classes: list = [permissions.IsAuthenticated,]
