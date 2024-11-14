from typing import Tuple, List, Dict
from django.db import models
from rest_framework import serializers

from el_shop.models import NetElement, Contact


class ContactSerializer(serializers.ModelSerializer):

    """
    Сериализатор для создания модели контактов сетевого элемента
    """

    class Meta:

        model: models.Model = Contact
        fields: List[str] = ["email", "country", "city", "street", "house_number"]


class NetElementCreateSerializer(serializers.ModelSerializer):

    """
    Сериализатор для создания модели сетевого элемента
    """

    supplier = serializers.SlugRelatedField(required=False, queryset=NetElement.objects.all(), slug_field="name")
    contact = ContactSerializer(required=False)

    class Meta:

        model: models.Model = NetElement
        read_only_fields: Tuple[str, ...] = ("id", "debt", "date_of_creation")
        fields: str = "__all__"

    def is_valid(self, *, raise_exception=False):

        """
        Проверка валидности сетевого элемента с контактом.
        """

        self._contact: Dict[str, str] = self.initial_data.pop("contact", {})
        self.initial_data["level"] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data: dict) -> NetElement:

        """
        Создание модели сетевого элемента с контактом
        """

        net_element: NetElement = NetElement.objects.create(**validated_data)
        net_element.save()

        contact: Contact = Contact.objects.create(
            base_class=net_element,
            email=self._contact.get("email", None),
            country=self._contact.get("country", None),
            city=self._contact.get("city", None),
            street=self._contact.get("street", None),
            house_number=self._contact.get("house_number", None)
            )
        contact.save()

        return net_element


class NetElementListSerializer(serializers.ModelSerializer):

    """
    Сериализатор для списка моделей сетевых элементов
    """

    supplier = serializers.SlugRelatedField(queryset=NetElement.objects.all(), slug_field="name")
    contact = ContactSerializer()

    class Meta:

        model: models.Model = NetElement
        fields: List[str] = ["id", "name", "level", "supplier", "debt", "contact"]


class NetElementSerializer(serializers.ModelSerializer):

    """
    Сериализатор для модели сетевого элемента
    """

    supplier = serializers.SlugRelatedField(required=False, queryset=NetElement.objects.all(), slug_field="name")
    contact = ContactSerializer(required=False)

    class Meta:

        model: models.Model = NetElement
        fields: str = "__all__"
        read_only_fields: Tuple[str, ...] = ("id", "debt", "date_of_creation", "level")

    def is_valid(self, *, raise_exception=False):

        """
        Функция для проверки валидности аргументов объекта сети
        """

        self._contact = self.initial_data.pop("contact", {})
        if "supplier" in self.initial_data:
            self.initial_data["level"] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def save(self):

        """
        Функция проверки и сохранения значений, содержащихся в аргументах контакта объекта сети
        """

        super().save()

        if self._contact != {}:
            self.instance.contact = self.update(self.instance.contact, self._contact)

        return self.instance


def level_detection(kwargs: dict) -> int:

    """
    Функция определения иерархического уровня элемента сети
    """

    level: int = 0
    if kwargs["supplier"] is None:
        return level

    supplier: NetElement = NetElement.objects.get(name=kwargs["supplier"])

    for i in range(2):
        level += 1
        if supplier.supplier is None:
            return level
        supplier = supplier.supplier

    raise Exception("Некорректное значение в иерархической системе")
