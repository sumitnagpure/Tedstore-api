# review/urls.py
from django.urls import path, include
from .views import ReviewView
from review.models import *


urlpatterns = [
    path("api/review", ReviewView.as_view(), name="employee-api"),
]


# curl -H "Authorization: Token 159cd5e529c0c42e54851403a1fcc400ccdb215d" http://localhost:8000/review/api/review
