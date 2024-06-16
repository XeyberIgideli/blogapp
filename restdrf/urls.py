from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # path('posts/', views.post_list),
    path('posts/', views.PostsListCreate.as_view()), # Generics View
    # path('posts/', views.PostsList.as_view()), # Generics View
    # path('add_post/', views.add_post),
    path('add_post/', views.AddPost.as_view()), # Generics View
    # path('post/<int:pk>', views.single_post),
    path('post/<int:pk>', views.SinglePost.as_view()), # Generics View
    
    path('post/update/<int:pk>', views.UpdatePost.as_view()), # Generics View
    path('post/delete/<int:pk>', views.DeletePost.as_view()), # Generics View
    # path('api-auth', views.obtain.as_view()),
    path('api-auth/', obtain_auth_token),
]