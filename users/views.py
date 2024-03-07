from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages, auth

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not Exist!')
            return redirect('loginUser')  

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Password!')
            return redirect('loginUser')    
    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'You are now log out')
    return redirect('loginUser')

@login_required(login_url='loginUser')
def profiles(request):
    return render(request, 'users/profiles.html')