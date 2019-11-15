from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .models import MyUser


""" This is for the form which will be for user login """
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

""" This form is for account registration for new user """
class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(label="Email:", widget=forms.EmailInput)
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password:",
                                widget=forms.PasswordInput)

    User = get_user_model()
    
    def clean_username(self):    
        user_provided_username = self.cleaned_data.get('username')
        
        #validation to check if username being registered already exists
        if User.objects.filter(username=user_provided_username):
            #if username exists, display error message
            raise forms.ValidationError("Username is already in use")
        return user_provided_username
    
    def clean_email(self):
        user_provided_email = self.cleaned_data.get('email')
        
        #validation to check if email address being registered already exists
        if User.objects.filter(email=user_provided_email):
            #if email address exists, display error message
            raise forms.ValidationError("Email address is already in use")
        return user_provided_email
    
    def clean_pasword2(self):
        password1 = self.cleaned.get('password1')
        password2 = self.cleaned.get('password2')
        
        #validation to ensure both password fields are entered
        if not password1 or not password2:
            raise ValidationError("Please enter passwords")
        
        #validation to ensure passwords matches    
        if password1 != password2:
            raise ValidationError("Passwords do not match")
        #returning password2 due to passing all validation
        return password2
    
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']