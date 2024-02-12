# order/urls.py
from django.urls import path, include
from .views import  OrderView
from .models import *

urlpatterns = [
    path('api/order',OrderView.as_view(), name='order-api')
]


# curl -H "Authorization: Token 35806b632bd790440eefa6be1bf50d872e355c36" http://localhost:8000/order/api/order