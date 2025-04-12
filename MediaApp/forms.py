from django import forms
from django.forms import ModelForm
from .models import MediaOutlet, Article

class MediaOutletForm(ModelForm):
    class Meta:
        model = MediaOutlet
        fields = '__all__'


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
