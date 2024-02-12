# review/urls.py
from django.urls import path, include
from .views import *
from review.models import *


urlpatterns = [
    path("all_review", ReviewAll, name="employee-api"),
    path("get_product_reviews", ProductReview, name="Product-Details"),
]


# curl -H "Authorization: Token 35806b632bd790440eefa6be1bf50d872e355c36" http://localhost:8000/review/api/review
