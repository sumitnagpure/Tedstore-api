from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Order) 

# @admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id",'user_id','date_ordered','status','total_amount')
admin.site.register(Order,OrderAdmin)
