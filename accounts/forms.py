from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from .models import Profile 



class SignupForm(UserCreationForm):
    class Meta:
       model = User
       fields = ('username', 'email', 'password1' , 'password2',)