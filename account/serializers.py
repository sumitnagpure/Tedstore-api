# account/serialzers.py

from rest_framework import serializers
from .models import account


class AccountSerializer(serializers.ModelSerializer):
    uid=serializers.IntegerField(source="user.id", read_only=True)
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.CharField(source="user.email", read_only=True)
    date_joined = serializers.CharField(source="user.date_joined", read_only=True)

    class Meta:
        model = account
        fields = ('uid',"first_name", "last_name", "email", "phone_number", "date_joined")
