from django.db import models

# Create your models here.

class Link(models.Model):
    originalLink = models.CharField(max_length=500)
    shortLink = models.CharField(max_length=8)