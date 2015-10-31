from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

# Create your views here.

from django.http import HttpResponse

# Home
def home(request):
    template = get_template('home.html')
    context = Context({})
    return HttpResponse(template.render(context))


# Products
def products_show(request, product):
    template = get_template('products/show.html')
    context = Context({'product': product})
    return HttpResponse(template.render(context))

def products_bridge(request, product):
    return HttpResponse('')


# Categories
def category_index(request):
    return HttpResponse('')

def category_show(request, category):
    return HttpResponse('')


# Brans
def brands_index(request):
    return HttpResponse('')

def brands_show(request, brand):
    return HttpResponse('')


# Editor's pick
def editor_index(request):
    return HttpResponse('')


#Spiders
def spiders_index(request):
	return HttpResponse('')

def spiders_scrape(request, spider):
	return HttpResponse('')