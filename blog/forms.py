from django import forms
from .models import BlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment', 'rating']

        