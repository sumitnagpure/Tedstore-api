# order/models.py
from django.db import models
from account.models import *

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    user_id = models.ForeignKey(account, on_delete=models.CASCADE, null=False)
    date_ordered = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "Orders"

    def __str__(self):
        return f"{self.id}"
