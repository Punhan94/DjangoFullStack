from django.contrib import admin
from .models import Sport, VideoSport

# Register your models here.

class VideoInline(admin.TabularInline):
    model = VideoSport

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    class Meta: model = Sport
    inlines = [ VideoInline]


@admin.register(VideoSport)
class VideoSportAdmin(admin.ModelAdmin):
    class Meta: model = VideoSport