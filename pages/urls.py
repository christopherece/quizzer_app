from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/<str:category>/<str:subcategory>/<int:user_id>/', views.index, name='index'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:score>/<int:total_questions>/<str:correct_answers>/', views.result, name='result'),
    path('check_attempt/', views.check_attempt, name='check_attempt'),


]
