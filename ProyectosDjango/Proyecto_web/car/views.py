from django.http import request
from django.shortcuts import render

from .car import Car
from store.models import Product

from django.shortcuts import redirect

# Create your views here.

def add_product(request, product_id):
    car=Car(request)
    product=Product.objects.get(id=product_id)
    car.add_car(product=product)
    return redirect('Store')

def remove_product(request, product_id):
    car=Car(request)
    product=Product.objects.get(id=product_id)
    car.remove_add(product=product)
    return redirect('Store')

def subtract_prod(request, product_id):
    car=Car(request)
    product=Product.objects.get(id=product_id)
    car.subtract_product(product=product)
    return redirect('Store')

def clean_car(request, product_id):
    car=Car(request)
    car.clean_car()
    return redirect('Store')