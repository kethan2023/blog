from django import forms
from blog.models import login_std,signup_std

class LoginForm(forms.ModelForm):
    class Meta:
        model=login_std
        fields=['user','password']

class SignupForm(forms.ModelForm):
    class Meta:
        model=signup_std
        fields=['firstname','lastname','email','contact','dob','user','password']