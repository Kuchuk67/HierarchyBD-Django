from django.db import models


class Products(models.Model):

    name_product: models.CharField = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Название товара",
        help_text="Название товара",
    )
    model_product: models.CharField = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="модель товара"
    )
    release_date: models.DateField = models.DateField(
        verbose_name="дата выхода на рынок",
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.name_product}/{self.model_product}"
