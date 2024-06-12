from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs', views.blog_index, name='blog_index'),
    path('blogs/<int:id>', views.blog_details, name='blog_details'),
]