from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view()
def products(request):
    search_str = request.GET.get('search')
    all = Product.objects.all()
    if search_str:
        all = all.filter(name__contains=search_str)
    all_products = ProductSerializer(all,many=True).data
    return Response(all_products)

