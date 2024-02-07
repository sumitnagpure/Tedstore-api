# order/views.py
from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Order.objects.all()
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
