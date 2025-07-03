from django.db import models


class Products(models.Model):
    
    name_product = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Название товара",
        help_text="Название товара",
    )
    model_product = models.CharField(max_length=100,
        null=False,
        blank=False,
        verbose_name="модель товара"
    )
    release_date = models.DateField(
        verbose_name="дата выхода на рынок",

        blank=False,
        )
