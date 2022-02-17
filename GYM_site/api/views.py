import django
from django.db.models import query
from django.shortcuts import get_object_or_404, render
from .serializers import ProductSerializer, UserSerializer, ArticleSerializer, SportSerializer
from rest_framework import serializers, viewsets
from shoppings.models import Product
from article.models import Article
from sports.models import Sport
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def patch(self, request, *args, **kvargs):
        product = Product.objects.get()
        data = request.data




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer
    permission_classes = ( IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(author=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.article_views +=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

