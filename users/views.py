from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print('Username or Password is incorrect')
    
    return render(request, 'users/login_register.html')


def profiles(request):
    return render(request, 'users/profiles.html')