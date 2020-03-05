from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import date 
from django.contrib.auth.models import User


class Entry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    entry = models.TextField()
    

    # def __str__(self):
    #     return self.title

class Prompt(models.Model):
    prompt = models.TextField()

