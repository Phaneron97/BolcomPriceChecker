from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def new(request):
    return HttpResponse('add new product')


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html')


def detail(request):
    return HttpResponse("Product detail")
