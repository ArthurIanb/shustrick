from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea())
    is_published = forms.BooleanField(label="Public")
    class Meta:
        model = Article
        fields = ['title', 'content', 'is_published']