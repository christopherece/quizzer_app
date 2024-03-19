from django.shortcuts import render,redirect
from users.models import StudentStats
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from datetime import datetime, timezone

@login_required(login_url='loginUser')
def index(request):
    student_stats = StudentStats.objects.filter(subcategory__created_by=request.user)
    context = {
        'student_stats': student_stats,
    }
    return render(request, 'teachers/index.html', context)
