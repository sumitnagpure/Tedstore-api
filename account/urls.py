# account/urls.py
from django.urls import path, include
from .views import AccountView
from account.models import *


urlpatterns = [
    path("all_accounts", AccountView.as_view(), name="employee-api"),
]


# curl -H "Authorization: Token 159cd5e529c0c42e54851403a1fcc400ccdb215d" http://localhost:8000/account/all_accounts