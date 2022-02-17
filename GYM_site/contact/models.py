from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Ours_Contact(models.Model):
    ours_location = models.CharField( max_length=100, blank=True)
    ours_coordinate = models.CharField(max_length=100, blank=True)
    ours_email = models.EmailField( max_length=254, blank=True)
    ours_mobil_telephone = models.CharField(max_length=50, blank=True)
    ours_office_phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.ours_email

class Contact(models.Model):
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    contact_subject = models.CharField(max_length=50, default='Şikayət')
    contact_email = models.EmailField()
    contact_detail = models.TextField()

    def __str__(self):
        return self.contact_email







