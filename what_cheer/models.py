from django.db import models
from datetime import date 
from django.contrib.auth.models import User
import time


class Entry(models.Model):
    def upload_image_name(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{self.owner}{round(time.time())}.{ext}'
        return f'what-cheer/{filename}'
    owner = models.ForeignKey(
    'auth.User', on_delete=models.CASCADE, related_name="entries")
    date = models.DateField(default=date.today)
    entry = models.TextField()
    image = models.ImageField(upload_to=upload_image_name, blank=True, null=True)

    


class Prompt(models.Model):
    prompt = models.TextField()

 