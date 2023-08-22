from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        search_str = request.GET.get('search')
        all = Product.objects.all()
        if search_str:
            all = all.filter(name__contains=search_str)
        all_products = ProductSerializer(all,many=True).data
        return Response(all_products)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view()
def categories(request):
    all_categories = CategorySerializer(Category.objects.all(), many=True).data
    return Response(all_categories)

