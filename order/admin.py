from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(order)
class order(models.ModelAdmin):
    list_display = ("id",)
