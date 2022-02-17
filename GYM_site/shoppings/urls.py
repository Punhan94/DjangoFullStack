from django.urls import path
from .views import all_products, with_category, product_detail, addComment

app_name='shoppings'

urlpatterns = [
    path('', all_products, name='all_products'),
    path('<slug:slug>/', with_category, name='with_category'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('add/<int:id>/', addComment, name='comment'),
]