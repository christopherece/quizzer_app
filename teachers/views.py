from django.shortcuts import render
from users.models import StudentStats

def index(request):
    student_stats = StudentStats.objects.all()
    context = {
        'student_stats': student_stats
    }
    return render(request, 'teachers/index.html', context)
