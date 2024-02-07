# account/serialzers.py

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "image",
            "base_price",
            "discounted_price",
            "in_stock",
            "tags",
            "details",
        )
