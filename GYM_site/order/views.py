from .models import Product
from django.contrib import messages
import random
import string
from django.http.response import HttpResponse, HttpResponseRedirect
from order.models import ShopCart, Order, OrderProduct
from order.forms import ShopCartForm, OrderForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

#butun sehiflerde gorunecek olanlar
def theCart(request):
    #yoxlayiriq eger user varsa
    if request.user.id:
        carts = ShopCart.objects.filter(user=request.user)
        shopCartsNavbar = ShopCart.objects.filter(user=request.user).order_by('-id')[:2]
        return{
            'carts':carts,
            'shopCartsNavbar':shopCartsNavbar,
        }
    return {}


@login_required(login_url='/user/login/')
def shopcarts(request):
    shopCarts = ShopCart.objects.filter(user = request.user )
    orderForm = OrderForm(request.POST or None)
    url = request.META.get('HTTP_REFERER')
    total = 0
    #shopcartdaki mallarin qiymetinin cemi hesablanmasi
    for i in shopCarts:
        total+=i.amount
    #sifaris formunun doldurulmasi
    if orderForm.is_valid():
        #eger shopcartdaki malin sayi stokdaki maldan cox olarsa
        for cart in shopCarts:
            if cart.quantity > cart.product.amount:
                cart.quantity = cart.product.amount
        total = 0
        #cemi de deyisdiririk
        for i in shopCarts:
            total+=i.amount
        data = orderForm.save(commit=False)
        data.user = request.user
        data.first_name = request.user.first_name
        data.last_name = request.user.last_name
        data.total = total
        data.ip = request.META.get('REMOTE_ADDR')
        ordercode = get_random_string(5).upper()
        data.code = ordercode
        data.save()

        #orderProductun yaradilmasi
        for i in shopCarts:
            detail = OrderProduct()
            detail.user = data.user
            detail.order_id = data.id
            detail.product_id = i.product_id
            detail.quantity = i.quantity
            detail.price = i.product.price
            detail.amount = i.amount
            detail.save()

            #malin stkodaki sayindan sifarisin cixilmasi
            product = Product.objects.get(id=i.product_id)
            product.amount -= i.quantity
            product.sold += i.quantity
            product.save()
        #sifaris ugurlu yerine yetdikde shopcartin silinmesi
        ShopCart.objects.filter(user = request.user).delete()
        messages.success(request, 'Sifarişiniz uğurla həyata keçirildi')
        return redirect('/article/userDashboard/')
    return render(request,'shopcarts.html', context={'shopCarts':shopCarts, 
        'total':total, 'orderForm':orderForm})

@login_required(login_url='/user/login/')
def addToCart(request, id):
    #ShopCarta elave etme funksiyasi
    url = request.META.get('HTTP_REFERER')
    item = ShopCart.objects.filter(user=request.user,product=id) 
    # yoxlayiriq eger hemin mal movcuddursa ustune elave edirik
    if item:
        olditem = ShopCart.objects.get(user=request.user, product=id)
        instance = ShopCart.objects.get(user=request.user, product=id)
        form = ShopCartForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance.quantity += olditem.quantity
            #yoxlayiriq eger say coxdursa stokdaki saya beraber edirik
            if instance.quantity > olditem.product.amount:
                instance.quantity = olditem.product.amount
                messages.warning(request, 'Maksimum sayda səbətə əlavə edilib.')
            form.save()
            return HttpResponseRedirect(url)
    else:
        #eger hemin mal stokda yoxdursa elave edirik
        form = ShopCartForm(request.POST or None)
        if form.is_valid():
            data = ShopCart()
            data.user = request.user
            data.product_id = id
            data.quantity = form.cleaned_data['quantity']
            data.save()
            return HttpResponseRedirect(url)

@login_required(login_url='/user/login/')
def deleteCart(request,id):
    #malin shopcartdan silinmesi
    ShopCart.objects.filter(user=request.user, product=id).delete()
    if ShopCart.objects.all():
        url = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(url)
    else:
        return render(request,'index.html')

@login_required(login_url='/user/login/')
#shopcartdaki malin sayinin deyisilmesi
def editCart(request, id):
    url = request.META.get('HTTP_REFERER')
    instance = ShopCart.objects.get(user=request.user, product=id)
    form = ShopCartForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance.quantity = form.cleaned_data['quantity']
        form.save()
        return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

#random funksiya 
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


