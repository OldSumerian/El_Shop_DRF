from datetime import datetime
from typing import List

from django.db import models

from config.settings import NULLABLE



class NetElement(models.Model):
    """
    Базовый класс для всех элементов сети
    """
    name = models.CharField(max_length=300, unique=True, verbose_name='Название')
    supplier = models.ForeignKey('self', **NULLABLE, default=None, on_delete=models.SET_DEFAULT,
                                 verbose_name='Поставщик')
    level = models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], verbose_name='Уровень в сети')
    debt = models.DecimalField(max_digits=12, decimal_places=2, default=0.00,
                               verbose_name='Задолженность перед поставщиком')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self) -> str:

        return self.name

    class Meta:

        abstract = False
        verbose_name: str = 'сетевой элемент'
        verbose_name_plural: str = 'сетевые элементы'
        ordering: List[str] = ['level']

    def save(self, *args, **kwargs):

        if not self.id:
            self.date_of_creation = datetime.now()
        return super().save(*args, **kwargs)


class Contact(models.Model):
    """
    Модель контакта у элемента сети
    """
    base_class = models.OneToOneField(NetElement, on_delete=models.CASCADE, **NULLABLE)
    email = models.EmailField(**NULLABLE, verbose_name='Почта')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=50, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=50, **NULLABLE, verbose_name='Улица')
    house_number = models.CharField(max_length=10, **NULLABLE, verbose_name='Номер дома')

    class Meta:

        verbose_name: str = 'контакт'
        verbose_name_plural: str = 'контакты'


class Product(models.Model):
    """
    Модель продукта у элемента сети
    """
    name = models.CharField(max_length=150, **NULLABLE, verbose_name='Наименование продукта')
    model = models.CharField(max_length=100, **NULLABLE, verbose_name='Модель')
    release_date = models.DateField()
    owner = models.ForeignKey(NetElement, on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self) -> str:

        return self.name

    class Meta:

        verbose_name: str = 'продукт'
        verbose_name_plural: str = 'продукты'
        ordering: List[str] = ['name','release_date']
