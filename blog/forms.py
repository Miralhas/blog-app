from django import forms
from .models import Post, Comment

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        labels = { 
            "title": "Title:",
            "content": "Content:"
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input border border-success"}),
            "content": forms.Textarea(attrs={"class": "form-input border border-success"}),
        }