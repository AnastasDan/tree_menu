from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Административная панель для отображения меню."""

    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    list_display_links = ("name",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Административная панель для отображения пунктов меню."""

    list_display = ("id", "name", "parent")
    search_fields = ("name", "slug")
    list_display_links = ("name",)
