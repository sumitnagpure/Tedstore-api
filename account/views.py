# Product/views.py
from django.shortcuts import render
from .models import *
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import F


# class AccountView(APIView):
#     # authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         data = account.objects.all()
#         serializer = AccountSerializer(data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def AccountView(request):
    if request.method == "GET":
        data = (
            account.objects.all()
            .annotate(
                first_name=F("user_id__first_name"), last_name=F("user_id__last_name")
            )
            .values("first_name", "last_name", "phone_number")
        )
        # serializers = AccountSerializer(data, many=True)
        return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def Subscribe(request):
    if request.method == "POST":
        email = request.data.get("email")

        if not email:
            return Response(
                {"error1": "email is required"}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            subscribers.objects.create(email=email)
            return Response({"message": f"Subscription successful for {subscribers.email}"}, status=status.HTTP_201_CREATED,)
        except Exception as e:
            return Response("error {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
