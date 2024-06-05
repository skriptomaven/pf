from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class Video(models.Model):
    title = models.CharField(max_length=47)
    description = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    date = models.DateField('date uploaded')
    comment = models.CharField(max_length=100)
