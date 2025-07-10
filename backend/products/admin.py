from django.contrib import admin

from products.models import Products


# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name_product", "model_product", "release_date")
    search_fields = ("name_product", "model_product", "release_date")
