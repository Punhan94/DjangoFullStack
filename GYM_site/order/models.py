from django.db.models.base import Model
from django.db.models.fields import CharField
from shoppings.models import Product
from django.db import models
from django import forms

# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    @property
    def amount(self):
        return (self.product.price * self.quantity)

    @property
    def price(self):
        return(self.product.price)


class Order(models.Model):
    status = (
        ('Yeni','New'),
        ('Qəbul edilmiş','Accepted'),
        ('Hazırlanır','Preaparing'),
        ('Karqoda','OnShipping'),
        ('Təhvil verilib','Completed'),
        ('Ləğv edilmiş','Canceled'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=14, editable=False)
    first_name = models.CharField(max_length=50, verbose_name='Adınız')
    last_name = models.CharField(max_length=50, verbose_name='Soyadınız')
    phone = models.CharField(blank=True, max_length=20,  verbose_name='Əlaqə nömrəsi')
    address = models.CharField( max_length=150, verbose_name='Adresiniz')
    city = models.CharField( max_length=30, verbose_name='Şəhər')
    total = models.FloatField()
    status = models.CharField(max_length=50, choices=status, default='Yeni')
    ip = models.CharField(blank=True, max_length=50)
    adminNote = models.CharField(blank=True, max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    status =(
        ('Yeni','New'),
        ('Qəbul edilmiş','Accepted'),
        ('Ləğv edilmiş','Canceled'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=20, choices=status, default='Yeni')
    create_at = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.product.title