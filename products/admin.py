from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
        'gender',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'ui_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
