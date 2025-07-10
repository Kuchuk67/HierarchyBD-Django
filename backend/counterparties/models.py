from django.db import models


class Counterparties(models.Model):
    name:models.CharField = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Название контрагента",
        help_text="Название контрагента",
        unique=False,
    )
    STATUS_CHOICES = [
        ("factory", "Завод"),
        ("retail", "Розничная продажа"),
        ("PE", "ИП"),
    ]
    that_is_type: models.CharField = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default="PE",
        verbose_name="Иерархия"
    )
    email: models.CharField = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="e-mail"
        )
    country: models.CharField = models.CharField(
        max_length=50,
        unique=False,
        verbose_name="страна"
        )
    city: models.CharField = models.CharField(
        max_length=50,
        unique=False,
        verbose_name="город"
        )
    street: models.CharField = models.CharField(
        max_length=50,
        unique=False,
        verbose_name="улица"
        )
    house_number: models.CharField = models.CharField(
        max_length=10,
        unique=False,
        verbose_name="номер дома"
    )
    active: models.BooleanField = models.BooleanField(
        verbose_name="контрагент активен"
        )

    def __str__(self) -> str:
        return f'{self.name}'
