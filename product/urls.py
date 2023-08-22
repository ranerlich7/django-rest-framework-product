from django.urls import path
from . import views
urlpatterns = [
    path('product', views.products, name='products'),
    path('product/<pk>', views.product_detail, name='product_detail'),
    path('category', views.categories,name='categories'),
]