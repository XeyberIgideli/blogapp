from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Category (models.Model):
    name = models.CharField(max_length=100)    