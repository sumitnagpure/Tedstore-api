# order/urls.py
from django.urls import path, include
from .views import  OrderView
from .models import *

urlpatterns = [
    path('api/order',OrderView.as_view(), name='order-api')
]


# curl -H "Authorization: Token 159cd5e529c0c42e54851403a1fcc400ccdb215d" http://localhost:8000/order/api/order