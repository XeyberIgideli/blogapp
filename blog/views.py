from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post,Category
# Create your views here. 

def index (request):
    categories = Category.objects.all() 
    return render(request, 'blog/index.html', {**{"title": "Home"}, **{"categories":categories}} )

def blog_index (request):
    data = {"posts": Post.objects.all()}
    return render(request, 'blog/blogs.html', {**{"title": "Blogs"}, **data} )

def blog_details (request, post_slug):
    # post = next((post for post in Post.objects.all() if post["id"] == id), None)   
    post = Post.objects.get(slug = post_slug)   
    return render(request, 'blog/blog-details.html', {**{"post": post}, **{"title": post.title}})

def blogs_by_category (request, category_slug): 
    # In Django, when you define a ForeignKey or a ManyToManyField relationship from one model to another, Django creates a manager on the related model to access related objects. 
    # The post_set is a manager that allows you to access all the Post objects related to a particular Category object.
    # data = Category.objects.get(slug = category_slug).post_set.filter(is_active = True) 
    data = Post.objects.filter(categories__slug = category_slug, is_active = True)  
    return render(request, 'blog/blogs.html', {**{"title": "Blogs"}, **{"posts":data}})
