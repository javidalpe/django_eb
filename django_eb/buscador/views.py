from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse("eb deploy")

def products_show(request, product):
    return HttpResponse("Product " + product)