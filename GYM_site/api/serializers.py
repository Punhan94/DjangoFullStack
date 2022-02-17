from django.db.models import fields
from rest_framework import serializers
from shoppings.models import Product
from article.models import Article
from sports.models import Sport
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['author']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

        extra_kwargs = {
            'password':{
                'write_only':True,
                'required':True
            }
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user


