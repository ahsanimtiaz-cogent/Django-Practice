from django.contrib import admin
from .models import Product, Category, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('condition', 'created_at')
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)