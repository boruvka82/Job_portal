from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    #phone = models.CharField(max_length=10)
    #image = models.ImageField(upload_to="")
    #gender = models.CharField(max_length=10)
    language = models.CharField(max_length=50)
    #level = dodelat zac,pokroc,konverzace..
    #type = models.CharField(max_length=15)

    #def __str__(self):
    #    return self.user.first_name

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #phone = models.CharField(max_length=10)
    #image = models.ImageField(upload_to="")
    #gender = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    language = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    about_me = models.CharField(max_length=100)

    #def __str__(self):
    #    return self.user.first_name

