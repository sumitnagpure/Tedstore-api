# product/models.py
from django.db import models


class tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Tags"


class details(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Details"


class product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    product_base_price = models.IntegerField()
    product_discounted_price = models.IntegerField()
    in_stock = models.BooleanField()
    tags = models.ForeignKey(
        tag, to_field="name", related_name="tags", on_delete=models.CASCADE
    )
    details = models.ForeignKey(
        details, to_field="name", related_name="details", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.title)
