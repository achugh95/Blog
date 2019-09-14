from django import forms
from . models import *


# ModelForm to create and edit the posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_date']
        widgets = {
            'created_date': forms.HiddenInput()
        }