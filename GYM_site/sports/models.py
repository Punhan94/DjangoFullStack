from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Sport(models.Model):
    title = models.CharField(max_length=200)
    slug= models.SlugField(null=True)
    content = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class VideoSport(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    detail = RichTextField(blank=True, null=True)
    video = models.FileField(upload_to='video/')