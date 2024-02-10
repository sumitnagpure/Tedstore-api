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


# curl -H "Authorization: Token 159cd5e529c0c42e54851403a1fcc400ccdb215d" http://localhost:8000/product/get_products


# sumit token
# 159cd5e529c0c42e54851403a1fcc400ccdb215d
