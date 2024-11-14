from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE

class User(AbstractUser):
    """
    Модель пользователя с переопределенным полем (email вместо username)
    """
    username = None
    email = models.EmailField(
        verbose_name="Электронная почта", unique=True, help_text="Введите адрес электронной почты"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефонный номер",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", **NULLABLE, help_text="Введите город"
    )
    avatar = models.ImageField(
        upload_to="users/", verbose_name="Аватар", **NULLABLE, help_text="Выберите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ["-date_joined", "-email"]

    def __str__(self):
        return f"Пользователь: {self.email}"

