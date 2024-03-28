from django import forms
from .models import Article

class AdminArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['art_title', 'art_content', 'art_image']
