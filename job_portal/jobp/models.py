from django.db import models
# from django.contrib.auth.models import User


class Teacher(models.Model):
    language_choices = (
        ("AJ", "Anglicky jazyk"),
        ("NJ", "Nemecky jazyk"),
        ("IT", "Italsky jazyk"),
        ("RJ", "Rusky jazyk"),
        ("FJ", "Francouzsky jazyk"),
        ("SJ", "Spanelsky jazyk"),
    )
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50, choices=language_choices)
    price = models.CharField(max_length=10)
    level = models.CharField(max_length=50, null=True, blank=True)
    about_me = models.CharField(max_length=250)
    # location = models.CharField(max_length=10)
    # image = models.ImageField(upload_to="")
    # gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
