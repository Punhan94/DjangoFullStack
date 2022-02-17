from django.urls import path

from shoppings.api.views import (PostListAPIViews, PostDetailAPIView, PostDeleteAPIView,
                                 PostUpdateAPIView, PostCreateAPIView)

app_name = 'api_shopping'

urlpatterns = [
    path('list/', PostListAPIViews.as_view(), name='list'),
    path('detail/<pk>/', PostDetailAPIView.as_view(), name='detail' ),
    path('delete/<pk>/', PostDeleteAPIView.as_view(), name='delete' ),
    path('update/<pk>/', PostUpdateAPIView.as_view(), name='update' ),
    path('create/', PostCreateAPIView.as_view(), name='create' ),
] 
