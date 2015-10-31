from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse("Hola Javi")

def products_show(request, product):
    template = get_template('products/show.html')
    context = Context({'product': product})
    return HttpResponse(template.render(context))


def spiders_index(request):
	return HttpResponse('')

def spiders_scrape(request, spider):
	return HttpResponse('')