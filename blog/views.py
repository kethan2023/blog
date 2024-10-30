from django.shortcuts import render
from blog.forms import *

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def profile(request):
    return render(request,'blog/profile.html')

def about(request):
    return render(request,'blog/about.html')

def newpost(request):
    return render(request,'blog/newpost.html')

def login_std(request):
    form=LoginForm()
    context={'form':form}
    return render(request,'blog/login.html',context)

def signup_std(request):
    form=SignupForm()
    context={'form':form}
    return render(request,'blog/signup.html',context)

