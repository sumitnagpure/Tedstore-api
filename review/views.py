# review/views.py
from pickle import GET
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

@api_view(["GET"])
# @permission_classes(IsAuthenticated)
def ReviewAll(request):
    if request.method == "GET":
        data = Review.objects.all()
        serializers = ReviewSerializer(data, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def ProductReview(request):
    if request.method == "GET":

        return Response(
            "Hello",
            status=status.HTTP_200_OK,
        )
