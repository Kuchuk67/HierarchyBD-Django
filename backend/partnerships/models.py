from django.db import models
from counterparties.models import Counterparties
from products.models import Products


# Create your models here.
class Partnerships(models.Model):
    person: models.ForeignKey = models.ForeignKey(
        Counterparties,
        null=True,
        blank=True,
        on_delete=models.RESTRICT,
        related_name="person",
        verbose_name="Контрагент",
    )
    supplier: models.ForeignKey = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.RESTRICT,
        related_name="supplier2",
        verbose_name="Контрагент",
    )
    products: models.ManyToManyField = models.ManyToManyField(
        Products,
        blank=True,
        related_name="products",
        verbose_name="Список продуктов, ID продукта: 1, 2 , 6",
        help_text="ID продукта: 1, 2 , 6",
    )
    debt: models.IntegerField = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="Задолженность поставщику"
    )
    data_create: models.DateTimeField = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return self.person.name
