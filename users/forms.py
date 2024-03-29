from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CustomUserCreationForm(UserCreationForm):
    UserType = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    user_type = forms.ChoiceField(choices=UserType)

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }