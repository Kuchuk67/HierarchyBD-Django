from django.db import models
from counterparties.models import Counterparties
# from partnerships.models import Partnerships as Supplier

# Create your models here.
class Partnerships(models.Model):
    person = models.ForeignKey(
        Counterparties, 
        null=True,
        blank=True,
        on_delete=models.RESTRICT,
        related_name="person", 
        verbose_name='Контрагент' 
        )
    supplier = models.ForeignKey(
        'self', 
        null=True,
        blank=True,
        on_delete=models.RESTRICT,
        related_name="supplier2", 
        verbose_name='Контрагент' 
        )
    #products = models.
    debt = models.ImageField(null=True, blank=True, default=0, verbose_name="Задолженность поставщику")
    data_create = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

