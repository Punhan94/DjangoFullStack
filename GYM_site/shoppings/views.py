from .models import Category, Images, Product, ShoppingComment
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def navbarCategory(request):
    categories = Category.objects.filter(parent__isnull=True)
    allProducts = Product.objects.all().order_by('-created_date')
    return{
        'categories':categories,
        'allProducts':allProducts,
    }

def all_products(request):
    filter = request.GET.get('filter', '-created_date')
    page = request.GET.get('page')
    p = Paginator(Product.objects.all().order_by(filter), 9)
    pagesProduct = p.get_page(page)
    return render(request, 'shopping.html', context={ 'pagesProduct':pagesProduct})

def with_category(request, slug):
    filter = request.GET.get('filter', '-created_date')
    page = request.GET.get('page', "1")
    with_categories = Category.objects.get(slug=slug)
    parent_category = Category.objects.filter(parent = with_categories)
    p = Paginator(Product.objects.filter(category=with_categories).order_by(filter), 6)
    pagesProduct = p.get_page(page)
    slug = slug
    return render(request, 'shopping.html', context={'with_categories':with_categories, 
            'pagesProduct': pagesProduct, 'slug':slug, 'parent_category':parent_category})

def product_detail(request,id):
    ProductComments = ShoppingComment.objects.filter(product_id=id)
    product = Product.objects.get(id=id)
    product.product_views +=1
    product.save()
    images = Images.objects.filter(product_id=id)
    return render(request, 'product_detail.html', context={'ProductComments':ProductComments, 
    'product':product,'images':images})


def addComment(request, id):
    if request.method == 'POST':
        content = request.POST.get('content')
        email = request.POST.get('email')
        name = request.POST.get('name')
        rate = request.POST.get('rating')
        new = ShoppingComment(comment_author=name,comment_email=email ,comment=content, product_id=id, rate=rate)
        new.save()
    return redirect('/shoppings/product/'+str(id))
