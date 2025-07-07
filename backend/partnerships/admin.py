from django.contrib import admin
from decimal import Decimal
from partnerships.models import Partnerships
from users.models import CustomUser
from django import forms

   

# Register your models here.
@admin.register(Partnerships)
class Partnerships(admin.ModelAdmin):

    def get_person_name(self, obj):
        return obj.person.name
    get_person_name.short_description = "Контрагент"

    def get_person_city(self, obj):
        return obj.person.city
    get_person_city.short_description = "Город"

    from django.urls import reverse
    def get_supplier_name(self, obj):
        if obj.supplier:
            from django.utils.html import format_html
            from django.urls import reverse

            url = reverse(
                f"admin:{obj.supplier.person._meta.app_label}_{obj.supplier.person._meta.model_name}_change",
                args=(obj.supplier.person.id,)
            )
            return format_html(
                '<a href="{}">{}</a>',
                url, 
                obj.supplier.person.name
                )
        else:
            return "-"
    get_supplier_name.short_description = "Поставщик"

    @admin.display(description="Цена, руб.")
    def get_debt_rub(self, obj):
        return Decimal(obj.debt) / 100


    list_display = ("get_person_city", "get_person_name", "get_debt_rub", "get_supplier_name", "data_create",)
    list_filter = ("person__city",)
    #list_editable = ("get_debt_rub",)
    #search_fields = ("name", "country", "city")

    '''@admin.display(description="Цена, руб.")
    def price_display(self, obj):
        # для отображения в списке
        return f"{obj.price/100:.2f}"'''
    


