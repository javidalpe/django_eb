from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse("Javi plantate un pino!!")

def products_show(request, product):
    template = get_template('products/show.html')
    context = RequestContext(request, {
        'product': product,
    })
    return HttpResponse(template.render(context))