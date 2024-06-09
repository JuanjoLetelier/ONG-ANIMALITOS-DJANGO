from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def formAdopcion(request):
    template = loader.get_template('formularioAdopcion.html')
    return HttpResponse(template.render())

def formRegistro(request):
    template = loader.get_template('formularioRegistro.html')
    return HttpResponse(template.render())

def formContacto(request):
    template = loader.get_template('formularioContacto.html')
    return HttpResponse(template.render())