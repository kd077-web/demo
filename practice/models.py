from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class practiceadmin(models.Model):
    title_icon=models.CharField(max_length=33)
    desc_icon=HTMLField()
news_slug=AutoSlugField(populate_from='title_icon',unique=True,null=True,default=None)    


# Create your models here.

