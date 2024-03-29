# review/serializer.py

from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "posted_by",
            "Product_id",
            "data",
            "post_date",
            "upvotes",
            "downvotes",
        )
