from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view


@api_view()
def products(request):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return Response(all_products)


@api_view()
def categories(request):
    all_categories = CategorySerializer(Category.objects.all(), many=True).data
    return Response(all_categories)

