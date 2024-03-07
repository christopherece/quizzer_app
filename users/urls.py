from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.loginUser, name='loginUser'),
    path('login/', views.logoutUser, name='logoutUser'),
    path('', views.profiles, name='profiles'),
]
