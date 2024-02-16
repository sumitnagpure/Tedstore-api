# account/urls.py
from django.urls import path, include
from .views import *
from account.models import *


urlpatterns = [
    # path("all_accounts", AccountView.as_view(), name="employee-api"),
    path("all_accounts/", AccountView, name="accountNames"),
    path("subscribed_users/", Subscribe, name = "SubscribedUsers"),
]


# curl -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" http://localhost:8000/account/all_accounts
# curl -X POST -H "Authorization: Token 1917df6373994418a4f0e687e31d02b62287bc91" -d email="first@email.com" http://localhost:8000/account/subscribed_users/