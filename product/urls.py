# Product/urls.py
from django.urls import path, include
from .views import *
from product.models import *


urlpatterns = [
    path("get_products", ProductView.as_view(), name="Product-api"),
    path("hero-section-slide", HeroSectionSlideView.as_view(), name="hero-section-slide"),
    path("get_subcategories", SubCategoriesView.as_view(), name="subcategories"),
    path('get_product_details', GetProductDetailsView.as_view(),name="ProductDetails"),
]


# curl -H "Authorization: Token 35806b632bd790440eefa6be1bf50d872e355c36" http://localhost:8000/product/get_products


# sumit token
# 35806b632bd790440eefa6be1bf50d872e355c36
