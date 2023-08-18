from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category, Product
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view


@api_view()
def products(request):
    search = request.GET.get('search')
    all_products = Product.objects.all()
    if search:
        all_products = all_products.filter(name__contains=search)
    all_products_json = ProductSerializer(all_products, many=True).data
    return Response(all_products_json)

@api_view()
def categories(request):
    all_categories = Category.objects.all()
    all_categories_json = CategorySerializer(all_categories, many=True).data
    return Response(all_categories_json)
    
    
