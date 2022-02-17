from django.urls import path
from .views import gym_center, all_gym  

urlpatterns = [
    path('',all_gym, name='all_gym'),
    path('<int:id>/', gym_center,name='gym_center')
]
