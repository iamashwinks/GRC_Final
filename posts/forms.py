from django import forms
from .models import Articles, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'summary', 'description', 'category', 'typename',)

class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('text',)