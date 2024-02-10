from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Review)
class review(admin.ModelAdmin):
    list_display = ("posted_by","product_id", "data", "post_date", "upvotes", "downvotes")
