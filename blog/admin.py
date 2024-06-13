from django.contrib import admin

from blog.models import Category, Post

from unfold.admin import ModelAdmin
from unfold.decorators import action, display
from django.utils.translation import gettext_lazy as _
from unfold.widgets import UnfoldAdminColorInputWidget 

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User 
from unfold.contrib.filters.admin import (
    ChoicesDropdownFilter,
    RangeDateFilter,
    RangeNumericFilter,
    RelatedDropdownFilter,
    SingleNumericFilter,
    TextFilter, 
    FieldTextFilter,
)


# Register your models here.
 
 
admin.site.unregister(User) 


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    search_fields = ["username", "first_name", "last_name", "email"]
    # list_filter = [
    #     FullNameFilter,
    #     ("status", ChoicesDropdownFilter),
    #     ("constructors", RelatedDropdownFilter),
    # ]
    # list_filter_submit = True
    # list_display = [
    #     "display_header",
    #     "display_constructor",
    #     "display_total_points",
    #     "display_total_wins",
    #     "display_status",
    #     "display_code",
    # ]
 
@admin.register(Post)
class PostAdmin(ModelAdmin):
        search_fields = ['title','categories__name', 'is_active', 'is_home', 'created_at', 'updated_at']
        list_filter_submit = True
        list_display = ['title','category', 'is_active', 'is_home', 'created_at', 'updated_at'] 
        list_filter = ( 
        ("created_at", RangeDateFilter), 
        ("categories__name", FieldTextFilter), 
         )
        
        def category(self, obj): 
            html = []
            
            for category in obj.categories.all():
                html.append(category.name)    
            if html == []:
                return "None"
            return html     

        # def get_form(self, request, obj=None, change=False, **kwargs):
        #     form = super().get_form(request, obj, change, **kwargs) 
        #     form.base_fields["color"].widget = UnfoldAdminColorInputWidget()
        #     return form

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
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
