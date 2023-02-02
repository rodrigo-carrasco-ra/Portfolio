from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/images/')
    body = models.TextField()
    created_at = models.DateTimeField(datetime.date.today)
    modified_at = models.DateTimeField(null=True,blank=True)
    slug = models.SlugField(null=True) 




