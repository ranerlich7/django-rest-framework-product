from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view()
def products(request):
    all_products = Product.objects.all()
    all_products_json = ProductSerializer(all_products, many=True).data
    return Response(all_products_json)
