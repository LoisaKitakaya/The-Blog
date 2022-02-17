from django import forms
from .models import *

# create your forms
class PostArticle(forms.ModelForm):

    class Meta:
    
        model = Article

        fieldS = '__all__'
        exclude = ['article_author', 'slug', 'posted_on']

class PostComment(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ['comment']