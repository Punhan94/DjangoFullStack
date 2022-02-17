from django import forms
from .models import Article, Comments, IndexCarousel

# from .models import Comments

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content','article_images']

class CarouselForm(forms.ModelForm):
    class Meta:
        model = IndexCarousel
        fields = ['carousel_title', 'carousel_content', 'carousel_images', 'carousel_button']

