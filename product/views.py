from django.shortcuts import render

from core.settings import REST_FRAMEWORK
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["GET"])
def AllProducts(request):
    if request.method == "GET":
        data = Product.objects.all()
        return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def HeroSectionSlide(request):
    if request.method == "GET":
        data = Product.objects.order_by("-id")[:1].values_list(
            "id", "title", "description", "Product__ProductImage_image"
        )
        return Response(data, status=status.HTTP_200_OK)
# Product.objects.order_by("-id")[:1].values_list("id", "title", "description","Product__ProductImage_image")

# {product_id:int, product_title:yy, product_description:yy, product_image:yy}, ..to 5 records}


@api_view(["GET"])
def SubCategories(request):
    if request.method == "GET":
        data = Product.objects.all()
        return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def GetProductDetails(request):
    if request.method == "GET":
        data = Product.objects.all()
        return Response(data, status=status.HTTP_200_OK)
