'''
Created on 26-Nov-2016

@author: sachin
'''
from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields =('title','text',)
        