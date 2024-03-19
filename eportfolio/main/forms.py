from django import forms
from .models import Student, Achievement
from django.contrib.auth.models import User


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description', 'completion_date', 'location', 'document']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=32)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']