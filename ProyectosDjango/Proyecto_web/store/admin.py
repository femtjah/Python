from django.contrib import admin
from .models import Product, CategoryProduct
# Register your models here.

class CategoryProdAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(CategoryProduct, CategoryProdAdmin)
admin.site.register(Product, ProductAdmin)