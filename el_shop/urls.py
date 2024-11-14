from django.urls import path
from el_shop import views
from el_shop.apps import ElShopConfig


app_name = ElShopConfig.name


urlpatterns = [
    path("", views.NetElementListView.as_view(), name='element_list'),
    path("create/", views.NetElementCreateView.as_view(), name='element_create'),
    path("node/<pk>", views.NetElementView.as_view(), name='element_detail'),
]