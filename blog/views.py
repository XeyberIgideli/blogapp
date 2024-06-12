from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post
# Create your views here.
postdata = {
    "blogs": [
        {"id": 1, "title": "How to be a Good Programmer"}, 
        {"id": 2, "title": "SQL Tutorial"},
        {"id": 3, "title": "Django Tutorial"}
    ]
}

def index (request):
    data = {"posts": Post.objects.all()}
    return render(request, 'blog/index.html', {"title": "Home"}, data)

def blog_index (request):
    data = {"posts": Post.objects.all()}
    return render(request, 'blog/blogs.html', {**{"title": "Blogs"}, **data} )

def blog_details (request, id):
    # post = next((post for post in Post.objects.all() if post["id"] == id), None)   
    post = Post.objects.get(id = id) 
    print(post)
    return render(request, 'blog/blog-details.html', {"post": post})
