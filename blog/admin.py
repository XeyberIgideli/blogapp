from django.contrib import admin

from blog.models import Category, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'is_home', 'created_at', 'updated_at')
    list_editable = ('is_active', 'is_home')
    search_fields = ('title', 'body')
    readonly_fields = ('created_at', 'updated_at', 'slug')
    list_per_page = 10
    
admin.site.register(Post, PostAdmin) 
admin.site.register(Category)
