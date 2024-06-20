from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os
from .models import Product
from .models import Brand

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def brands(request):
    brands = Brand.objects.all()
    return render(request, 'main/brands.html', {'brands': brands})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})

def contacts(request):
    return render(request, 'main/contacts.html')