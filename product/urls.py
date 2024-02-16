# Product/urls.py
from django.urls import path, include
from .views import *
from product.models import *


urlpatterns = [
    path("get_products/", AllProducts, name="all-Products-api"),
    path("hero_section_slide/", HeroSectionSlide, name="hero_section_slide"),
    path("get_subcategories/<int:category_id>", SubCategories, name="subcategories"),
    path('get_product_details/', GetProductDetails,name="ProductDetails"),
    path('get_offers/', GetOffers, name="get_offers"),
]


# curl -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" http://localhost:8000/product/get_products
# curl -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" http://localhost:8000/product/hero_section_slide/
# curl -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" http://localhost:8000/product/get_subcategories/
# curl -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" http://localhost:8000/product/get_offers/


# sumit token
# 1917df6373994418a4f0e687e31d02b62287bc91
