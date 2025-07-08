from decimal import Decimal
from django import forms
from django.contrib import admin
from partnerships.models import Partnerships
from django.urls import reverse
from django.utils.html import format_html


class PartnershipsAdminForm(forms.ModelForm):
    # Заменяем поле debt, чтобы вводить/показывать в рублях
    debt = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        label="Долг (руб.)",
        help_text="Введите сумму долга в рублях. В базе она хранится в копейках.",
    )

    class Meta:
        model = Partnerships
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # При редактировании делим копейки на 100
        if self.instance and self.instance.pk is not None:
            # Перекладываем сконвертированное value в initial
            self.initial["debt"] = (Decimal(self.instance.debt) / 100).quantize(
                Decimal("0.01")
            )

    def clean_debt(self):
        # При сохранении умножаем рубли на 100
        debt_rub = self.cleaned_data.get("debt") or Decimal("0.00")
        return int((debt_rub * 100).quantize(Decimal("1")))


@admin.action(description="Удалить задолжность")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


# Register your models here.
@admin.register(Partnerships)
class Partnerships(admin.ModelAdmin):
    form = PartnershipsAdminForm

    def get_person_name(self, obj):
        return obj.person.name

    get_person_name.short_description = "Контрагент"

    def get_person_city(self, obj):
        return obj.person.city

    get_person_city.short_description = "Город"

    def get_supplier_name(self, obj):
        if obj.supplier:
            url = reverse(
                (
                    f"admin:{obj.supplier.person._meta.app_label}"
                    f"_{obj.supplier.person._meta.model_name}_change"
                ),
                args=(obj.supplier.person.id,),
            )
            return format_html('<a href="{}">{}</a>', url, obj.supplier.person.name)
        else:
            return "-"

    get_supplier_name.short_description = "Поставщик"

    @admin.display(description="Цена, руб.")
    def get_debt_rub(self, obj):
        return Decimal(obj.debt) / 100

    list_display = (
        "get_person_city",
        "get_person_name",
        "get_debt_rub",
        "get_supplier_name",
        "data_create",
    )
    list_filter = ("person__city",)

    actions = [clear_debt]
