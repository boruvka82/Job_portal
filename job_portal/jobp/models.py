from django.db import models
# from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    language1 = models.CharField(max_length=50)
    language2 = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=10)
    level = models.CharField(max_length=50, null=True, blank=True)
    about_me = models.CharField(max_length=250)
    # location = models.CharField(max_length=10)
    # image = models.ImageField(upload_to="")
    # gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

