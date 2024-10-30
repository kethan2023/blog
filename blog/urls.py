from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns=[
    path('',index,name='index'),
    path('profile',profile,name='profile'),
    path('about',about,name='about'),
    path('newpost',newpost,name='newpost'),
    path('login_std',login_std,name='login_std'),
    path('signup_std',signup_std,name='signup_std')
]
