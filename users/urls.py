from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('logout/', views.loginUser, name='loginUser'),
    path('login/', views.logoutUser, name='logoutUser'),
    path('register/', views.registerUser, name='registerUser'),
    path('', views.profiles, name='profiles'),
    path('admin/logout/',views.admin_logout, name='admin_logout'),  



]
