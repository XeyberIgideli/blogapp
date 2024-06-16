from rest_framework import serializers
from blog.models import Post
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    lowercase_title = serializers.SerializerMethodField(read_only=True) 
    # title = serializers.CharField(validators=[])
    class Meta:
        model = Post
        fields = ['id', 'title', 'body','is_active','is_home', "uppercase_title","lowercase_title"] 
     
     
    # def validate_title (self, value):
    #     qs = Post.objects.filter(title__iexact = value) # iexact = case insensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exists")
    #     return value
     
    def get_lowercase_title(self, obj):  
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj,Post):
            return None
        return obj.lowercase_title() 
    
class TokenSerializer (serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'password']