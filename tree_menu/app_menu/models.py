from django.db import models


class Menu(models.Model):
    """Модель для представления меню."""

    name = models.CharField("Название меню", max_length=255, unique=True)
    slug = models.SlugField("Идентификатор", max_length=255)

    class Meta:
        ordering = ("id",)
        verbose_name = "меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Модель для представления пункта меню."""

    name = models.CharField("Название пункта меню", max_length=255)
    slug = models.SlugField("Название пункта идентификатора", max_length=255)

    menu = models.ForeignKey(
        Menu,
        blank=True,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="Меню",
    )
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="childrens",
        on_delete=models.CASCADE,
        verbose_name="Родительский пункт меню",
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name
