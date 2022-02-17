from django.db.models.query import QuerySet
from rest_framework import permissions, serializers
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView,
                                     DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView)
from shoppings.api.paginations import ProductPagination
from shoppings.api.permissions import IsOwner
from rest_framework.filters import OrderingFilter, SearchFilter
from shoppings.api.serializers import ShoppingsSerializer
from ..models import Product
from rest_framework.permissions import IsAdminUser


class PostListAPIViews(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ShoppingsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    # searchFilter axtaris, orederingfilter siralama
    search_fields = ['title', 'detail']
    pagination_class = ProductPagination
    

class PostDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ShoppingsSerializer
    lookup_field = 'pk'
    

class PostDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ShoppingsSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ShoppingsSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]

class PostCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ShoppingsSerializer
    permission_classes = [IsAdminUser]