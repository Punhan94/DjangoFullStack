from django.shortcuts import render, HttpResponse
from article.models import Article
from shoppings.models import Product
from sports.models import Sport
from gym_center.models import GymCenter
from gym_center.models import GymCenter, Images
import json

# Create your views here.

def index(request):
    random_gymCenter = GymCenter.objects.order_by('?')[0]
    random_gym_images = Images.objects.filter(gym_center_id=random_gymCenter.id)[0]
    return render(request, 'index.html', context={'random_gym_images':random_gym_images,
                                                  'random_gymCenter':random_gymCenter})

def idealceki(request):
    return render(request, 'idealceki.html')

def all_search(request):
    keyword = request.GET.get('searched')
    if keyword:
        searched_articles = Article.objects.filter(title__icontains=keyword)
        searched_products = Product.objects.filter(title__icontains=keyword)
        searched_sports = Sport.objects.filter(title__icontains=keyword)
        searched_gymcenter = GymCenter.objects.filter(center_name__icontains=keyword)
        return render(request, 'searchPage.html', context={
            'searched_articles':searched_articles, 'searched_products':searched_products,
            'searched_gymcenter':searched_gymcenter,'searched_sports':searched_sports
        })

def all_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        searched_articles = Article.objects.filter(title__icontains=q)
        searched_products = Product.objects.filter(title__icontains=q)
        searched_sports = Sport.objects.filter(title__icontains=q)
        searched_gymcenter = GymCenter.objects.filter(center_name__icontains=q)
        results = []
        def elaveET(x):
            for i in x:
                place_json = {}
                place_json = i.title
                results.append(place_json)
            data = json.dumps(results)
        elaveET(searched_articles)
        elaveET(searched_products)
        elaveET(searched_sports)
        for i in searched_gymcenter:
            place_json = {}
            place_json = i.center_name
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)