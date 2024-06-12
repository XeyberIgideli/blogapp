from django.db import models
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}" 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class Category (models.Model):
    name = models.CharField(max_length=100)  
      
    def __str__(self):
        return f"{self.name}" 