from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs', views.blog_index, name='blog_index'),
    path('blogs/<slug>', views.blog_details, name='blog_details'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)