from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import get_user_model

#Import login_required annotations
from django.contrib.auth.decorators import login_required

# Create your views here.

""" This is the landing page for user account """
def index(request):
    return render(request, "accounts/index.template.html")

""" This is the logout function """
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(index)
    
""" This is the user login function """
def login(request):
    if request.method == "POST":
        #This will populate the login request with the user input into the login form
        login_form = UserLoginForm(request.POST)
        
        #If the login form input is valid
        if login_form.is_valid():
            #check if the user name and password match
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            #If user exists, log them in
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.template.html', {
            'form': form
        })
        
@login_required
def profile(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)
    return render(request, "accounts/profile.template.html", {
        'user': user
    })
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            pass
        else:
            return render(request, "accounts/register.template.html", {
                'form': form
            })
    else:   
        register_form = UserRegistrationForm()
        return render(request, "accounts/register.template.html", {
            'form': register_form
        })
    
    