from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    del list_display[list_display.index('description')]
    del list_display[list_display.index('characteristic')]
    list_filter = ['category', 'price_per_some']
    search_fields = ['name', 'price']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class PricePerSomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PricePerSome._meta.fields]

    class Meta:
        model = PricePerSome


admin.site.register(PricePerSome, PricePerSomeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
