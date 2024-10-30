from django.db import models

# Create your models here.

class login_std(models.Model):
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=16)

class signup_std(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    contact=models.IntegerField()
    dob=models.DateField()
    user=models.CharField(max_length=20)
    password=models.CharField(max_length=16)
