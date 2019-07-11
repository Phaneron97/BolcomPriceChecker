from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def new(request):
    return HttpResponse('add new product')


"""
gets 'product' which has all objects from 'Product' table stored,
passes is to index.html for it be shown in the frontend
"""
def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'products': product})


def detail(request):
    return HttpResponse("Product detail")
