from django.db import models
from tinymce.models import HTMLField




class services(models.Model):
    title=models.CharField(max_length=33)
    desc=models.TextField

# Create your models here.
