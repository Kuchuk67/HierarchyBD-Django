from decimal import Decimal
from django import forms
from django.contrib import admin
from partnerships.models import Partnerships
from counterparties.models import Counterparties
from django.urls import reverse
from django.utils.html import format_html
from typing import Any
#from django.contrib.admin import ModelAdmin
from django.http import HttpRequest
from django.db.models.query import QuerySet

class PartnershipsAdminForm(forms.ModelForm):
    # Заменяем поле debt, чтобы вводить/показывать в рублях
    debt = forms.DecimalField(
        max_digits=14,
        decimal_places=2,
        label="Долг (руб.)",
        help_text="Введите сумму долга в рублях. В базе она хранится в копейках.",
    )

    class Meta:
        model = Partnerships
        fields = "__all__"


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # При редактировании делим копейки на 100
        if self.instance and self.instance.pk is not None:
            # Перекладываем сконвертированное value в initial
            self.initial["debt"] = (Decimal(self.instance.debt) / 100).quantize(
                Decimal("0.01")
            )


    def clean_debt(self) -> int:
        # При сохранении умножаем рубли на 100
        debt_rub = self.cleaned_data.get("debt") or Decimal("0.00")
        return int((debt_rub * 100).quantize(Decimal("1")))


@admin.action(description="Удалить задолжность")
def clear_debt(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet) -> None:
    queryset.update(debt=0)


# Register your models here.
@admin.register(Partnerships)
class PartnershipsAdmin(admin.ModelAdmin):
    form = PartnershipsAdminForm


    @admin.display(description="Контрагент")
    def get_person_name(self, obj: Partnerships) -> str:
        assert isinstance(obj.person, Counterparties)  # подсказываем mypy
        return obj.person.name
    

    @admin.display(description="Город")
    def get_person_city(self, obj: Partnerships) -> str:
        assert isinstance(obj.person, Counterparties)  # подсказываем mypy
        return obj.person.city


    from typing import cast
    @admin.display(description="Поставщик")
    def get_supplier_name(self, obj: Partnerships) -> str:
        if obj.supplier:
            assert isinstance(obj.supplier.person, Counterparties)
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


    @admin.display(description="Цена, руб.")
    def get_debt_rub(self, obj: Partnerships) -> Decimal:
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
