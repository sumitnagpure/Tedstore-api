# product/urls.py
from django.urls import path, include
from .views import ProductView
from product.models import *


urlpatterns = [
    path("api/product", ProductView.as_view(), name="product-api"),
]


# curl -H "Authorization: Token 75a6c6e111fae68b93aae82330b725df2779a353" http://localhost:8000/product/api/product

# sumit token
# 75a6c6e111fae68b93aae82330b725df2779a353
