# Product/urls.py
from django.urls import path, include
from .views import *
from product.models import *


urlpatterns = [
    path("get_products/", AllProducts, name="all-Products-api"),
    path("hero_section_slide/", HeroSectionSlide, name="hero_section_slide"),
    path("get_subcategories/<int:category_id>", SubCategories, name="subcategories"),
    path('get_product_details', GetProductDetails,name="ProductDetails"),
]


# curl -H "Authorization: Token 35806b632bd790440eefa6be1bf50d872e355c36" http://localhost:8000/product/get_products
# curl -H "Authorization: Token 35806b632bd790440eefa6be1bf50d872e355c36" http://localhost:8000/product/hero_section_slide/
# curl -H "Authorization: Token 35806b632bd790440eefa6be1bf50d872e355c36" http://localhost:8000/product/get_subcategories/


# sumit token
# 35806b632bd790440eefa6be1bf50d872e355c36
