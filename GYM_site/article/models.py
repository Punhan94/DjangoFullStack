from re import match
from typing import Match
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE
from django.contrib import auth
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class IndexCarousel(models.Model):
    carousel_images = models.FileField(blank=True, null=False, verbose_name='Sekil elave edin')
    carousel_title = models.CharField(max_length=50)
    carousel_content = models.CharField(max_length=100)
    carousel_button = models.CharField(max_length=20)

    def __str__(self):
        return self.carousel_title

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    article_rate = models.PositiveIntegerField(default=0)
    article_views = models.PositiveIntegerField(default=0)
    articles_likes = models.PositiveIntegerField(default=0)
    article_images = models.FileField( null=True, verbose_name='Sekil elave edin')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @(property)
    def rated(self):
        comment_rate = Comments.objects.filter(article = self)
        rate =0
        rated=0
        cem=0
        for i in comment_rate:
            rated += i.rate
            cem +=1
        if cem >0 and rated >0:
            rate = round(rated/cem) 
        if rate >0:
            self.article_rate = rate
            self.save()
            return (rate)
        else:
            return('None')


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Məqalə', related_name='comments')
    comment_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rate = models.IntegerField(default=1,
            validators=[
                MaxValueValidator(5),
                MinValueValidator(0)
            ]
    )
    comment = models.TextField()
    comment_created_date = models.DateTimeField(auto_now_add=True)

class LikeArticle(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True )
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
