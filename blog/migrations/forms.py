from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #field = '__all__'
        fields = ('author', 'message')