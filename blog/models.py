from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=100)  
    slug = models.SlugField(null=False, blank=True, unique=True,editable=False, db_index=True)
      
    def __str__(self):
        return f"{self.name}" 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()
    image = models.ImageField(upload_to="blog", null=True)
    slug = models.SlugField(null=False, blank=True, unique=True,editable=False, db_index=True) 
    categories = models.ManyToManyField(Category, blank=True)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}" 
    
    @property
    def uppercase_title(self):
        return self.title.upper()
    
    def lowercase_title(self): 
        return self.title.lower()
    
    def save(self, *args, **kwargs):  
        self.slug = slugify(self.title) 
        super().save(*args, **kwargs) 
    
