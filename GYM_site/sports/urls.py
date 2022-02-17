from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sports_index, name='sports_index'),
    path('<slug:slug>/', views.sport_detail, name='sport_detail'),
    path('axtaris/<int:id>/', views.sports, name='sports')
]
