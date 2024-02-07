from django.contrib import admin
from .models import *


# Register your models here.
# @admin.register(Product)
# class Product(admin.ModelAdmin):
#     list_display = (
#         "title",
#         "description",
#         "image",
#         "base_price",
#         "discounted_price",
#         "in_stock",
#         "tags",
#         "details",
#     )


# @admin.register(Tag)
# class tag(admin.ModelAdmin):
#     list_display = ["tag_id","name"]
admin.site.register(Tag)
admin.site.register(Details)
admin.site.register(Product)

# @admin.register(Details)
# class details(admin.ModelAdmin):
#     list_display = ["name"]
