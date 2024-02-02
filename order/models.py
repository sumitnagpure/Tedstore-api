from django.db import models


class order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    user_id = models
    date_ordered = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, defaul="pending")
    total_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
