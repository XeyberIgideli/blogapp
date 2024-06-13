from django.contrib import admin

from blog.models import Category, Post

from unfold.admin import ModelAdmin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User 
# Register your models here.
 
 
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass
 
@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'is_active', 'is_home', 'created_at', 'updated_at')
#     list_editable = ('is_active', 'is_home')
#     readonly_fields = ('created_at', 'updated_at', 'slug')
#     search_fields = ('title', 'body')
#     list_per_page = 10


# class CategoryAdmin (admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#     list_per_page = 10 
    
# admin.site.register(Post, PostAdmin) 
# admin.site.register(Category, CategoryAdmin)
