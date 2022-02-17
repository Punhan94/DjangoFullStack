from django import forms
from .models import Order, ShopCart

class ShopCartForm(forms.ModelForm):
    class Meta:
        model= ShopCart
        fields = ['quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['city','address', 'phone']