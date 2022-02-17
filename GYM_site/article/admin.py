from django.contrib import admin
from django.db import models
from django.db.models.expressions import OrderBy
from .models import Article, Comments, IndexCarousel, LikeArticle, Comments

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class Meta: model = Article
    list_display = ['title', 'author']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    class Meta: model = Comments
    list_display = ['comment_author']

@admin.register(IndexCarousel)
class CarouselAdmin(admin.ModelAdmin):
    class Meta: model = IndexCarousel
    list_display = ['carousel_title']

@admin.register(LikeArticle)
class LikeArticleAdmin(admin.ModelAdmin):
    class Meta: model = LikeArticle
