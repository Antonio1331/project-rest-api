from django.contrib import admin

from .models import Category, Product, Brand, Color


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Color)