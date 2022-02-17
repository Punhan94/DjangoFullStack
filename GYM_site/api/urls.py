from django.db import router
from django.urls import path, include
from .views import ProductViewSet, UserViewSet,ArticleViewSet, SportViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('user', UserViewSet, basename='user' )
router.register('articles', ArticleViewSet, basename='articles' )
router.register('sports', SportViewSet, basename='sports' )

urlpatterns = [
    path('', include(router.urls) ),
]
