from cProfile import label
from cgitb import text
from dataclasses import fields
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "user_email", "text"]
        label = {
            "user_name":"your name",
            "user_email":"your email",
            "text":"your comment",
        }