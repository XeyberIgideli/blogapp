from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from blog.models import Post

# Token
from django.contrib.auth.models import User
from .authentication import TokenAuthentication, AdvancedToken

# Rest Framework 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer 
from rest_framework import mixins

from rest_framework import generics, mixins, permissions 
from .permissions import isOwnerOrReadOnly
# Create your views here.

# API VIEW FUNCTION

# @api_view(['GET'])
# def post_list(request):
#     instance = Post.objects.all().order_by('?').first() 
#     data = {}
#     if instance:
#         data = PostSerializer(instance).data
#     return Response(data)

# @api_view(['POST'])
# def add_post(request):
#     serializer = PostSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         return Response(serializer.data)

# class obtain_token (generics.ListAPIView):
#     user = User.objects.filter(username = 'pardaillan')
#     serializer_class = TokenSerializer
#     # token = Token.objects.create(user=user)
#     print(user)    

# GENERICS VIEW CLASSES 
from rest_framework.authtoken.views import ObtainAuthToken
                
class obtain (ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = AdvancedToken.objects.get_or_create(user=user)
        return Response({'token': token.key})             

# Get post by id
class SinglePost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [isOwnerOrReadOnly] 
      
    
# Create post    
class AddPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]

    def perform_create (self, serializer):  
        return serializer.save()
      

# Get all posts    
class PostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

# Get all posts and add new post        
class PostsListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# Update post        
class UpdatePost(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer        

# Delete post
class DeletePost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer        
    lookup_field = 'pk' 
    
    def perform_destroy (self, instance):
        super().perform_destroy(instance)
 
# MIXINS VIEW CLASSES

# Mixin single post by id
class MixinSinglePost(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)               
        