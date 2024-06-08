from django.db import models
from django.contrib.auth.models import AbstractUser


class FlixUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Video(models.Model):
    title = models.CharField(max_length=47)
    description = models.TextField()
    comment = models.TextField()
    author = models.ForeignKey(FlixUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/')
