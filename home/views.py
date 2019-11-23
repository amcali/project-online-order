from django.shortcuts import render, HttpResponse

# Create your views here.

""" Renders Landing page """
def home(request):
    return render(request, "home/index.template.html")
    
""" Renders About page """
def about_us(request):
    return render(request, "home/about_us.template.html")