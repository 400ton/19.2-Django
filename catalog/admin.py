from django.contrib import admin
from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'preview')
    list_filter = ('name', 'price', 'category')
    search_fields = ('name', 'description', 'category', 'price')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number', 'name',)
    list_filter = ('product', 'name',)
    search_fields = ('product', 'number', 'name',)
