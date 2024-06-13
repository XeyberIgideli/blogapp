from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs', views.blog_index, name='blogs'),
    path('blogs/<slug:post_slug>', views.blog_details, name='blog_details'),
    path('blogs/category/<slug:category_slug>', views.blogs_by_category, name='blog_by_category'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)