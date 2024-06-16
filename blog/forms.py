from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = '__all__' # ['title', 'body', 'is_active', 'is_home']

    def clean(self):
        title = self.cleaned_data['title'] 
        if Post.objects.filter(title = title).exists():
            raise forms.ValidationError({'title': "This title already exists!"})