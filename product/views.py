from django.shortcuts import render
import json
from core.settings import REST_FRAMEWORK
from django.http import JsonResponse
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
        latest_product = Product.objects.order_by("-id").first()
        if latest_product:
            product_images = latest_product.productimages_set.all()
            if product_images:
                data = {
                    "id": latest_product.id,
                    "title": latest_product.title,
                    "description": latest_product.description,
                    "images": [img.image.url for img in product_images],
                }
                return Response(data, status=status.HTTP_200_OK)


# Product.objects.order_by("-id")[:1].values_list("id", "title", "description","Product__ProductImage_image")


@api_view(["GET"])
def SubCategories(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategories_A = {}
    subcategories_B = {}
    subcategories_A_queryset = SubcategoryA.objects.filter(category=category)
    for subcategory in subcategories_A_queryset:
        if subcategory.name in subcategories_A:
            subcategories_A[subcategory.name].append(
                {"sub_category_id": subcategory.id, "value": subcategory.value}
            )
        else:
            subcategories_A[subcategory.name] = [
                {"sub_category_id": subcategory.id, "value": subcategory.value}
            ]
    subcategories_B_queryset = SubcategoryB.objects.filter(category=category)
    for subcategory in subcategories_B_queryset:
        if subcategory.name in subcategories_B:
            subcategories_B[subcategory.name].append(
                {"sub_category_id": subcategory.id, "value": subcategory.value}
            )
        else:
            subcategories_B[subcategory.name] = [
                {"sub_category_id": subcategory.id, "value": subcategory.value}
            ]
    return JsonResponse(
        {"Subcategory_A": subcategories_A, "Subcategory_B": subcategories_B}
    )


@api_view(["GET"])
def GetProductDetails(request):
    if request.method == "GET":
        data = Product.objects.all()
        return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def GetOffers(request):
    if request.method == "GET":
        offers = Offer.objects.all()
        data = list()
        for offer in offers:
            offer_data = {
                "offer_id": offer.id,
                "offer_category": offer.category,
                "offer_description": offer.description,
            }
            data.append(offer_data)
        return Response(data, status=status.HTTP_200_OK)
    # [ {offer_id:int, offer_category: lorem, offer_description:lorem}, ..to 2 records ]
