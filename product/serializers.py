# account/serialzers.py

from rest_framework import serializers
from .models import product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ('title', 'description', 'image', 'product_base_price','product_discounted_price','in_stock','tags','details')