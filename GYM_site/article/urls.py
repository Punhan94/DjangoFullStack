from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('create/', views.createArticle, name='create'),
    path('editArticle/<int:id>/', views.editArticle, name='editArticle'),
    path('deleteArticle/<int:id>/', views.deleteArticle, name='deleteArticle'),
    path('viewArticle/<int:id>/', views.viewArticle, name='viewArticle'),
    path('userDashboard/', views.userDashboard, name='userDashboard'),
    path('comment/<int:id>/', views.addComment, name='comment'),
    path('allarticle/', views.all_article, name='allarticle'),
    path('likeArticle/<int:id>', views.likeArticle, name='likeArticle'),
    path('unlikeArticle/<int:id>', views.unlikeArticle, name='unlikeArticle'),
    path('likeArticles/',views.likeArticles, name='likeArticles' ),
    path('editcomment/<int:id>/', views.editArticle)
]
