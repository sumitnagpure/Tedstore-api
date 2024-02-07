# Product/urls.py
from django.urls import path, include
from .views import ProductView
from product.models import *


urlpatterns = [
    path("all_products", ProductView.as_view(), name="Product-api"),
]


# curl -H "Authorization: Token 159cd5e529c0c42e54851403a1fcc400ccdb215d" http://localhost:8000/product/all_products

# sumit token
# 159cd5e529c0c42e54851403a1fcc400ccdb215d
