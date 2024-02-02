# review/urls.py
from django.urls import path, include
from .views import ReviewView
from review.models import *


urlpatterns = [
    path("api/review", ReviewView.as_view(), name="employee-api"),
]


# curl -H "Authorization: Token 75a6c6e111fae68b93aae82330b725df2779a353" http://localhost:8000/review/api/review

# sumit token
# 75a6c6e111fae68b93aae82330b725df2779a353
