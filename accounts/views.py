from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UsernameField
from accounts.forms import SignupForm
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid:
            form.save()

            username=form.cleaned_data('username')
            password=form.cleaned_data('password')

            user =authenticate(username=username, password=password)
            login(request,user)

            return redirect('/accounts/profile')

    
    else:
        form = signup_form()

    return(request, 'registration/signup.html', {'form':form})



def profile(request):
    pass



def edit_profile(request):
    pass