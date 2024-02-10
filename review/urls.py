# review/urls.py
from django.urls import path, include
from .views import *
from review.models import *


urlpatterns = [
    path("all_review", ReviewView.as_view(), name="employee-api"),
    path("get_product_reviews", ProductDetails.as_view(), name="Product-Details")
]


# curl -H "Authorization: Token 159cd5e529c0c42e54851403a1fcc400ccdb215d" http://localhost:8000/review/api/review
