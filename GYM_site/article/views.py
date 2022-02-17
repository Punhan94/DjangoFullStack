from django.db.models.query import EmptyQuerySet
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import IndexCarousel, Article, Comments, LikeArticle
from order.models import OrderProduct
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def footer(request):
    formm = Article.objects.all().order_by('-created_date')[:3]
    random_article = Article.objects.order_by('?')[0]
    allArticles = Article.objects.all().order_by('-created_date')
    carousel = IndexCarousel.objects.all()
    return{
        'formm':formm,
        'carousel': carousel,
        'allArticles':allArticles,
        'random_article':random_article
    }
    
#meqale elave etmek
@login_required(login_url='/user/login/')
def createArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Məqalə uğurla əlavə olundu')
        return redirect(userDashboard)
    return render(request, 'createArticle.html', context={'form': form})

#meqalede deyisiklik etmek
@login_required(login_url='/user/login/')
def editArticle(request, id):
    instance = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(userDashboard)
    return render(request, 'editArticle.html', context={'form': form})

#meqaleni silmek
@login_required(login_url='/user/login/')
def deleteArticle(request, id):
    Article.objects.filter(id=id, user=request.user).delete()
    return redirect(userDashboard)

#meqaleni oxumaq
def viewArticle(request, id):
    form = get_object_or_404(Article, id=id)
    form.article_views +=1
    form.save()
    itsArticleLike = LikeArticle.objects.filter(article_id=id)
    comments = form.comments.all().order_by('-comment_created_date')
    return render(request, 'viewArticle.html', context={'form': form, 
                    'comments': comments, 'itsArticleLike':itsArticleLike })

#istifadeci sehifesi
@login_required(login_url='/user/login/')
def userDashboard(request):
    form = Article.objects.filter(author=request.user).order_by('-created_date')
    orderedProducts = OrderProduct.objects.filter(user=request.user)
    return render(request, 'userDashboard.html', context={'form': form,'orderedProducts':orderedProducts})

#butun meqaleler
def all_article(request):
    filter = request.GET.get('filter','-created_date')
    page = request.GET.get('page')
    p = Paginator(Article.objects.all().order_by(filter), 9)
    allarticle = p.get_page(page)
    return render(request, 'allArticle.html',context={'allarticle':allarticle})

#meqaleye serh yazmaq
@login_required(login_url='/user/login/')
def addComment(request, id):
    article = get_object_or_404(Article, id=id)
    comments = Comments.objects.filter(article=article, comment_author=request.user).count()
    if request.method == 'POST' and comments != 1:
        c_content = request.POST.get('c_content')
        c_rating = request.POST.get('rating')
        new = Comments(comment_author=request.user, comment=c_content, rate=c_rating)
        article.rated
        new.article = article
        new.save()
    return redirect('/article/viewArticle/'+str(id))

#meqalede deyisiklik etmek
@login_required(login_url='/user/login/')
def editArticle(request, id):
    filterComment = Comments.objects.filter(id=id, comment_author=request.user)
    if filterComment:
        instance = Comments.objects.get(id=id, comment_author=request.user )
        article = get_object_or_404(Article, id=instance.article.id)
        if request.method=='POST':
            c_content = request.POST.get('c_content')
            c_rating = request.POST.get('rating')
            instance.rate = c_rating
            instance.comment = c_content
            article.rated
            instance.save()
            return redirect('/article/viewArticle/'+str(article.id))
        else:
            form = article
            itsArticleLike = LikeArticle.objects.filter(article_id=form.id)
            comments = form.comments.all().order_by('-comment_created_date')
        return render(request, 'viewArticle.html', context={'form': form, 
                        'comments': comments, 'itsArticleLike':itsArticleLike, 
                        'instance':instance })
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)

#meqaleni beyenmek
@login_required(login_url='/user/login/')
def likeArticle(request, id):
    if LikeArticle.objects.filter(article_id=id, user=request.user):
        pass
    else:
        article = Article.objects.get(id=id)
        article.articles_likes +=1
        article.save()
        newLike = LikeArticle(article_id = id, user=request.user)
        newLike.save()
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)

#beyenilen meqalelerin butun sehifelerde istifadesi
def allLikeArticles(request):
    if request.user.id:
        likeArticlenavbar = LikeArticle.objects.filter(user=request.user).order_by('-id')[:2]
        likeArticles = LikeArticle.objects.filter(user=request.user)
        return{
            'likeArticles':likeArticles,
            'likeArticlenavbar':likeArticlenavbar,
        }
    else:
        return{}

#meqalenin beyenilmesini geri cekmek
@login_required(login_url='/user/login/')
def unlikeArticle(request,id):
    LikeArticle.objects.filter(article_id=id, user=request.user).delete()
    article = Article.objects.get(id=id)
    article.articles_likes -=1
    article.save()
    url = request.META.get('HTTP_REFERER')
    if LikeArticle.objects.filter(user=request.user):
        return HttpResponseRedirect(url)
    else:
        return redirect('/article/allarticle/')

#butun beyenilen meqaleler
def likeArticles(request):
    return render(request, 'likesArticle.html')


