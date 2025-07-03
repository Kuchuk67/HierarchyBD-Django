'''from django.db import models

# Create your models here.
class Partnerships(models.Model):
    person = models.
    supplier = models.
    products = models.
    debt = models.ImageField(null=True, blank=True, default=0, verbose_name="Задолженность поставщику")
    data_create = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")'''

from django.db import models
from counterparties.models import Counterparties
from treebeard.mp_tree import MP_Node
# from partnerships.models import Partnerships

class Partnerships(MP_Node):
    person = models.ForeignKey(
        Counterparties, 
        null=True,
        blank=True,
        on_delete=models.RESTRICT,
        related_name="person", 
        verbose_name='Контрагент' )
    
    # name = models.CharField(max_length=30)
    # node_order_by = ['data_create']

    #debt = models.ImageField(null=True, blank=True, default=0, verbose_name="Задолженность поставщику")
    #data_create = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return 'Partnerships: {}'.format(self.person)