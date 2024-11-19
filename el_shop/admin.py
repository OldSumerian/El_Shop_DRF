from typing import Tuple, List, Union
from django.contrib import admin
from django.db import models
from django.db.models import QuerySet
from django.utils.html import format_html

from el_shop.models import NetElement, Contact, Product


class ContactInline(admin.TabularInline):
    """
    Класс для вкладки контактов в административную панель
    """
    model: models.Model = Contact
    extra = 0


class ProductInline(admin.TabularInline):
    """
    Класс для вкладки продуктов в административную панель
    """
    model: models.Model = Product
    extra = 0


class NetElementAdmin(admin.ModelAdmin):
    """
    Класс для кастомизации административной панели сетевого элемента
    """
    inlines: List[admin.TabularInline] = [ContactInline, ProductInline,]
    list_display: Tuple[str, ...] = ("id", "name", "level", "to_supplier", "debt")
    list_display_links: Tuple[str, ...] = ('name', 'to_supplier')
    list_filter: Tuple[str, ...] = ('contact__city', )
    fields: List[Union[Tuple[str, ...], str]] = [("id", "name"),
                                                 ("level", "supplier"),
                                                 "debt",
                                                 "date_of_creation"]
    readonly_fields: Tuple[str, ...] = ("id", "date_of_creation",)
    search_fields: Tuple[str, ...] = ("name",)
    save_on_top: bool = True
    actions: List[str] = ['clear_dept']

    def to_supplier(self, obj: NetElement):
        """
        Функция по возвращению HTML-ссылки для поставщика
        """
        if obj.supplier is not None:
            return format_html(
                '<a href="/admin/el_shop/element/{id}">{name}</a>',
                id=obj.supplier.id,
                name=obj.supplier
            )


    @admin.action(description='clear debt')
    def clear_dept(self, request, queryset: QuerySet) -> None:
        """
        Функция для очистки долга к поставщику
        """
        queryset.update(debt=0)


class ProductAdmin(admin.ModelAdmin):
    """
    Класс для кастомизации административной панели продукта
    """
    list_display: Tuple[str, ...] = ("name", "model", "release_date", "owner")
    list_display_links = ('name', 'owner')
    search_fields: Tuple[str, ...] = ("name", "model", "release_date")
    save_on_top = True


admin.site.register(NetElement, NetElementAdmin)
admin.site.register(Product, ProductAdmin)
