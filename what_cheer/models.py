from django.db import models
from datetime import date 
from django.contrib.auth.models import User


class Entry(models.Model):
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name="entries")
    date = models.DateField(default=date.today)
    entry = models.TextField()
    


class Prompt(models.Model):
    prompt = models.TextField()

