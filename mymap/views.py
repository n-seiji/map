from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import buildmap

def buildmap(request):
    return osm

def hello(request):
    return HttpResponse("Hello, world. You're at the hello.")
