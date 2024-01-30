from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(account)
class Account(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date_joined", "phone_number")
    @admin.display(ordering="first_name",description="First name")
    def first_name(self,obj):
        return obj.first_name
    @admin.display(ordering="last_name",description="Last name")
    def last_name(self,obj):
        return obj.last_name
    @admin.display(ordering="email", description="Email address")
    def email(self,obj):
        return obj.email
    @admin.display(ordering="date_joined", description="Date Joined")
    def date_joined(self,obj):
        return obj.date_joined