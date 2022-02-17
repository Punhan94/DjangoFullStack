from django.db import models
from order.models import ShopCart, Order, OrderProduct
from django.contrib import admin

# Register your models here.

@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    class Meta: model=ShopCart
    list_display = ['product','quantity','amount','price']
    
@admin.register(OrderProduct)
class OrderProdcatAdmin(admin.ModelAdmin):
    class Meta: model=OrderProduct
    list_display = ['product','quantity','amount','price', 'status']
    list_editable = ['status']

class OrderProductLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('product', 'price','quantity','amount')
    can_delete = False
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    class Meta: model=Order
    list_display = ['code','first_name','last_name','address','status']
    list_editable = ['status']
    readonly_fields = ('code','first_name','last_name','address','phone','city','total','ip')
    can_delete = False
    inlines = [OrderProductLine]


