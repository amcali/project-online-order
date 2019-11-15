from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import MyUser


""" This is for the form which will be for user login """
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

""" This form is for account registration for new user """
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password:",
                                widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']