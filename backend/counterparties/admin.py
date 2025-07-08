from django.contrib import admin

from counterparties.models import Counterparties


# Register your models here.
@admin.register(Counterparties)
class Counterparties(admin.ModelAdmin):
    list_display = ("name", "that_is_type", "country", "city", "email")
    list_filter = (
        "country",
        "city",
        "that_is_type",
    )
    search_fields = ("name", "country", "city")
