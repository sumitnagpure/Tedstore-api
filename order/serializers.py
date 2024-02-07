# review/serialzers.py

from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user_id','date_ordered','status','total_amount','created_at','updated_at')