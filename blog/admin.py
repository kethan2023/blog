from django.contrib import admin
from blog.models import login_std,signup_std

# Register your models here.

@admin.register(login_std)
class login_std(admin.ModelAdmin):
    list_display=['user','password']


@admin.register(signup_std)
class signup_std(admin.ModelAdmin):
    list_display=['firstname','lastname','email','contact','dob','user','password']