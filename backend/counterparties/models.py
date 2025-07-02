from django.db import models


class Counterparties(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Название продукта",
        help_text="Название продукта",
    )
    STATUS_CHOICES = [
        ("factory", "Завод"),
        ("retail", "Розничная продажа"),
        ("PE", "ИП"),
    ]
    that_is_type = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default="PE",
        verbose_name="Иерархия"
    )
    email = models.CharField(max_length=150,
        unique=False,
        verbose_name="e-mail"
    )
    country = models.CharField(max_length=50,
        unique=False,
        verbose_name="страна"
    )
    city = models.CharField(max_length=50,
        unique=False,
        verbose_name="город"
    )
    street = models.CharField(max_length=50,
        unique=False,
        verbose_name="улица"
    )
    house_number = models.CharField(max_length=10,
        unique=False,
        verbose_name="номер дома"
    )
    active = models.BooleanField(
        verbose_name="контрагент активен"
    )

    place = models.CharField(
        max_length=50,
        default=None,
        null=True,
        blank=True,
        verbose_name="место выполнения привычки",
        help_text="место, в котором необходимо выполнять привычку",
    )

    time_action = models.TimeField(
        default=None,
        null=True,
        blank=True,
        verbose_name="время выполнения привычки",
        help_text="время, когда необходимо выполнять привычку",
    )
    period = models.CharField(
        max_length=50,
        default="1,2,3,4,5,6,7",
        blank=True,
        verbose_name="день недели, когда необходимо выполнять привычку",
        help_text="дни недели через запятую 1,2,3,4,5,6,7",
    )
