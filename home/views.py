from django.shortcuts import render, HttpResponse

# Create your views here.

""" Renders Landing page """
def index(request):
    return HttpResponse("Hello World. This is the home page")