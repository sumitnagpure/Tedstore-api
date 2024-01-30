from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(review)
class review(admin.ModelAdmin):
    list_display = ("posted_by", "data", "post_date", "upvotes", "downvotes")
