from django.shortcuts import render,redirect
from users.models import StudentStats
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from datetime import datetime, timezone
from django.contrib import messages, auth


@login_required(login_url='loginUser')
def index(request):
    if request.user.is_authenticated and request.user.profile.user_type == 'Teacher':
        student_stats = StudentStats.objects.filter(subcategory__created_by=request.user)
        context = {
            'student_stats': student_stats,
        }
        return render(request, 'teachers/index.html', context)
    else:
        messages.error(request, 'You are not permitted to access that page!')
        return redirect('profiles')