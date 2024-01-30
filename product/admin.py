from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(product)
class Product(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image",
        "product_base_price",
        "product_discounted_price",
        "in_stock",
        "tags",
        "details",
    )
@admin.register(tag)
class tag(admin.ModelAdmin):
    list_display=['name']

@admin.register(details)
class details(admin.ModelAdmin):
    list_display=['name']
