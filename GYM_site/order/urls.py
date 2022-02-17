from django.urls import path
from .views import  shopcarts, addToCart, deleteCart, editCart

app_name='order'

urlpatterns = [
    path('', shopcarts, name='shopcarts'),
    path('addtocart/<int:id>/', addToCart, name='addToCart'),
    path('deleteCart/<int:id>', deleteCart, name='deleteCart'),
    path('editcart/<int:id>/', editCart, name='editCart'),
]