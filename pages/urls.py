from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('dashboard/<str:category>/<str:subcategory>/<int:user_id>/', views.index, name='index'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('result/<int:score>/<int:total_questions>/<str:correct_answers>/', views.result, name='result'),

]
