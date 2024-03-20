from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pages.models import Category, Subcategory, Question, Option
from users.models import StudentStats
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group


from django.contrib import messages, auth

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_staff = True
            user_type = form.cleaned_data['user_type']  # Get the user_type from the form
            user.save()
            #Save to Profile
            user.profile.user_type = user_type  # Assuming profile is related_name in User model
            user.profile.save()

            messages.success(request, 'You are now registered and can log in')
            if user_type == 'Teacher':
                 # Add the user to TeacherGroup
                teacher_group = Group.objects.get_or_create(name='Teacher_Admin')[0]
                teacher_group.user_set.add(user)
                login(request, user)
                return redirect('/admin/')
            else:
                login(request, user)
                return redirect('profiles')

        else:
            messages.error(request, 'An error occured during registration')
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context)

# Create your views here.
def loginUser(request):
    page = 'login'

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
            return redirect('profiles')
        else:
            messages.error(request, 'Invalid Password!')

            return redirect('loginUser')    
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'You are now log out')
    return redirect('loginUser')

@login_required(login_url='loginUser')
def profiles(request):
    if request.user.is_authenticated:
        categories = Category.objects.filter(is_active=True).prefetch_related('subcategory_set', 'question_set__option_set').order_by('is_active')
        subcategories = Subcategory.objects.values('name','exam_date','is_active').order_by('name') 
        studstats = StudentStats.objects.filter(user=request.user)
        student_stats = StudentStats.objects.filter(subcategory__created_by=request.user)

        context = {
            'categories': categories,
            'studstats':studstats,
            'subcategories':subcategories,
            'student_stats':student_stats,
        }
        return render(request, 'users/profiles.html', context)



