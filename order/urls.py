# order/urls.py
from django.urls import path, include
from .views import  OrderView
from .models import *

urlpatterns = [
    path('api/order',OrderView.as_view(), name='order-api')
]


# curl -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" http://localhost:8000/order/api/order