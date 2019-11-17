from django.shortcuts import render, HttpResponse

# Create your views here.

""" Renders Landing page """
def home(request):
    return render(request, "home/index.template.html")