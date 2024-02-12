# account/urls.py
from django.urls import path, include
from .views import *
from account.models import *


urlpatterns = [
    # path("all_accounts", AccountView.as_view(), name="employee-api"),
    path("all_accounts/", AccountView, name="accountNames"),
    path("subscribed_users/", Subscribe, name = "SubscribedUsers"),
]


# curl -H "Authorization: Token 35806b632bd790440eefa6be1bf50d872e355c36" http://localhost:8000/account/all_accounts