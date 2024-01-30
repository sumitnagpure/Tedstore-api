from django.db import models
from account.models import *

# Create your models here.
class review(models.Model):
    posted_by = models.ForeignKey(account, related_name="posted_by", on_delete=models.CASCADE)
    data = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    class Meta:
        verbose_name_plural = "Reviews" 
