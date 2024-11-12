from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE

class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Email address", unique=True, help_text="Input email address"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone number",
        **NULLABLE,
        help_text="Input phone number",
    )
    city = models.CharField(
        max_length=50, verbose_name="City", **NULLABLE, help_text="Input city"
    )
    avatar = models.ImageField(
        upload_to="users/", verbose_name="Avatar", **NULLABLE, help_text="Choose avatar"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-date_joined", "-email"]

    def __str__(self):
        return f"User: {self.email}"

