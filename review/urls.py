# review/urls.py
from django.urls import path, include
from .views import *
from review.models import *


urlpatterns = [
    path("all_review", ReviewAll, name="employee-api"),
    path("get_product_reviews", ProductReview, name="Product-Details"),
]


# curl -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" http://localhost:8000/review/api/review
