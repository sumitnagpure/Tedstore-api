# Product/models.py
from unittest.util import _MAX_LENGTH
from django.db import models


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return str(self.name)


class Details(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        verbose_name_plural = "Details"

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Category"


class SubcategoryA(models.Model):
    category = models.ForeignKey(
        Category, related_name="subcategory_A", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name + " " + self.value)

    class Meta:
        verbose_name_plural = "SubCategory A"


class SubcategoryB(models.Model):
    category = models.ForeignKey(
        Category, related_name="subcategory_B", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name + " " + self.value)

    class Meta:
        verbose_name_plural = "SubCategory B"


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_a = models.ForeignKey(SubcategoryA, on_delete=models.CASCADE)
    subcategory_b = models.ForeignKey(SubcategoryB, on_delete=models.CASCADE)
    base_price = models.IntegerField()
    discounted_price = models.IntegerField()
    in_stock = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="Products")
    details = models.ForeignKey(
        Details, to_field="name", related_name="Details", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.title)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")

    class Meta:
        verbose_name_plural = "Product-Images"
