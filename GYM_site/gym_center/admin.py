from django.contrib import admin
from django.db import models
from .models import GymCenter,Images, Contact, WorkDay

# Register your models here.

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 3

class ContactInline(admin.TabularInline):
    model = Contact

class WorkDayInline(admin.TabularInline):
    model = WorkDay
    extra = 6

@admin.register(GymCenter)
class GYMAdmin(admin.ModelAdmin):
    class Meta: model = GymCenter
    inlines = [ImagesInline, ContactInline, WorkDayInline ]


@admin.register(Images)
class IMGAdmin(admin.ModelAdmin):
    class Meta: model = Images

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    class Meta: model = Contact

@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    class Meta: model = WorkDay


