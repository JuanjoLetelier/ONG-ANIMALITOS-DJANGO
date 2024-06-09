from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def carritoAdopcion(request):
    template = loader.get_template('carritoAdopcion.html')
    return HttpResponse(template.render())