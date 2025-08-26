from django.shortcuts import render
from .models import Product
# Create your views here.

def home(request):
    return render(request, "home.html")


def product_list(request):
    products = Product.objects.first()  
    return render(request, "products.html", {"products": products})