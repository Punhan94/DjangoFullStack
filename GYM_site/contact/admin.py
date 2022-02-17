from django.contrib import admin
from .models import Contact, Ours_Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    class Meta: model = Contact

@admin.register(Ours_Contact)
class Ours_ContactAdmin(admin.ModelAdmin):
    class Meta: model = Ours_Contact