from django.db import models
from account.models import account
from product.models import *


# Create your models here.
class Review(models.Model):
    posted_by = models.ForeignKey(
        account, related_name="posted_by", on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product, related_name="Product_id", on_delete=models.CASCADE
    )
    data = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

    class Meta:
        verbose_name_plural = "Reviews"
