"""django_eb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    #Landings, Javi's land
    url(r'^$', 'buscador.views.home'),
    url(r'^productos/(?P<product>[0-9]+)/$', 'buscador.views.products_show'),

    url(r'^categorias/$', 'buscador.views.category_index'),
    url(r'^categorias/(?P<category>[a-z]+)/$', 'buscador.views.category_show'),

    url(r'^marcas/$', 'buscador.views.brands_index'),
    url(r'^marcas/(?P<brand>[a-z]+)/$', 'buscador.views.brands_show'),

    url(r'^editor/$', 'buscador.views.editor_index'),


    #Spiders, Alvaro's land
    url(r'^spiders/', 'buscador.views.spiders_index'),
    url(r'^spiders/(?P<spider>[0-9]+)/$', 'buscador.views.spiders_scrape'),

    url(r'^admin/', include(admin.site.urls)),
]
