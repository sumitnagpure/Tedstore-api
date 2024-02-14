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
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ("product", "image")


admin.site.register(Tag)
admin.site.register(Details)
admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(SubcategoryA)
admin.site.register(SubcategoryB)
# admin.site.register(ProductImages)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
