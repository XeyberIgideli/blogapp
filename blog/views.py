from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post
# Create your views here. 

def index (request):
    data = {"posts": Post.objects.all()}
    return render(request, 'blog/index.html', {**{"title": "Home"}, **data} )

def blog_index (request):
    data = {"posts": Post.objects.all()}
    return render(request, 'blog/blogs.html', {**{"title": "Blogs"}, **data} )

def blog_details (request, slug):
    # post = next((post for post in Post.objects.all() if post["id"] == id), None)   
    post = Post.objects.get(slug = slug)   
    return render(request, 'blog/blog-details.html', {**{"post": post}, **{"title": post.title}})
