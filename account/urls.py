# account/urls.py
from django.urls import path, include
from .views import AccountView
from account.models import *


urlpatterns = [
    path("api/account", AccountView.as_view(), name="employee-api"),
]


# curl -H "Authorization: Token 75a6c6e111fae68b93aae82330b725df2779a353" http://localhost:8000/account/api/account

# sumit token
# 75a6c6e111fae68b93aae82330b725df2779a353
