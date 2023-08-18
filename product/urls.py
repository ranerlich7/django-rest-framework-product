from django.urls import path
from . import views
urlpatterns = [
    path('product', views.products, name="products"),
    path('create_product', views.create_product, name="create_product"),
    path('category', views.categories, name="categories"),    
]