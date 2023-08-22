from django.urls import path
from . import views
urlpatterns = [
    path('product', views.products, name='products'),
    path('category', views.categories,name='categories'),
]