from django.urls import path
from . import views
urlpatterns = [
    path('product', views.products, name='products'),
    path('product/create', views.create_product,name='create_product'),
    path('category', views.categories,name='categories'),
]