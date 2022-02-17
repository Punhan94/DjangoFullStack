from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class GymCenter(models.Model):
    center_name = models.CharField(max_length=50)
    center_logo = models.ImageField(blank=True, upload_to ='images/' )
    center_images = models.ImageField(blank=True, upload_to ='images/' )
    map_address = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    detail = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.center_name

class Images(models.Model):
    gym_center = models.ForeignKey(GymCenter, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    gym_center = models.ForeignKey(GymCenter, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.number

class WorkDay(models.Model):
    gym_center = models.ForeignKey(GymCenter, on_delete=models.CASCADE)
    DOW_CHOICES = (
        ( ("Bazar ertəsi"),1),
        ( ("Çərşənbə axşamı"),2),
        ( ("Çərşənbə"),3),
        (("Cümə axşamı"),4),
        ( ("Cümə"),5),
        ( ("Şənbə"),6),
        ( ("Bazar"),7),
    )
    day_of_week = models.CharField(max_length=50,
        choices=DOW_CHOICES)
    work_day_hours = models.CharField(max_length=20)

    def __str__(self):
        return self.work_day_hours