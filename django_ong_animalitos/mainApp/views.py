from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def adoptame(request):
    template = loader.get_template('adoptame.html')
    return HttpResponse(template.render())

