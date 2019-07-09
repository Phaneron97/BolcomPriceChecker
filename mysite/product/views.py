from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def new(request):
    return HttpResponse('add new product')


def index(request):
    return HttpResponse("All products in list")
