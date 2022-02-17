from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from article import views
from .views import index, idealceki, all_search, all_search_auto
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('idealceki/', idealceki, name='idealceki'),
    path('article/', include('article.urls')),
    path('user/', include('user.urls')),
    path('shoppings/', include('shoppings.urls', namespace='shoppings')),
    path('gymCenter/', include('gym_center.urls')),
    path('order/',include('order.urls')),
    path('contact/',include('contact.urls')),
    path('sports/', include('sports.urls')),
    path('search/', all_search , name='all_search'),
    path('search_auto/', all_search_auto, name='all_search_auto'),
    path('api/', include('api.urls') ),
    path('auth/', obtain_auth_token)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
