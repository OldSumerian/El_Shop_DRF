from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("el_shop.urls", namespace="el_shop")),
    path("users/", include("users.urls", namespace="users")),
]
