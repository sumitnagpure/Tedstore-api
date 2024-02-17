from django.shortcuts import render
from core.settings import REST_FRAMEWORK
from django.http import JsonResponse

import product
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["GET"])
def AllProducts(request):
    if request.method == "GET":
        data = Product.objects.all().values("title")
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
        product_title = request.GET.get("product_title")

        product = Product.objects.get(title=product_title)
        response_data = {
            "product_id": product.id,
            "product_title": product.title,
            "product_description": product.description,
            "product_base_price": product.base_price,
            "product_discounted_price": product.discounted_price,
            "in_stock": product.in_stock,
            "product_tags": [{"tags_id": tag.id, "tags_name": tag.name} for tag in product.tags.all()],
            "product_details": product.details,
            "product_images": [img.image.url for img in product.productimages_set.all()],
            "product_features_images": [img.image.url for img in product.featuresimages_set.all()],
            "product_specifications": [{"name": spec.name, "value": spec.value} for spec in product.specifications.all()]
        }
        # data = Product.objects.all()
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
def GetOffers(request):
    if request.method == "GET":
        offers = Offer.objects.all().values("category","description")
        return Response(offers, status=status.HTTP_200_OK)
    # [ {offer_id:int, offer_category: lorem, offer_description:lorem}, ..to 2 records ]
