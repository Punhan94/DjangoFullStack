from django.db.models import fields
from rest_framework import serializers

from shoppings.models import Product

class ShoppingsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'api_shopping:detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Product
        fields = '__all__'
        
    # username = serializers.SerializerMethodField()
    # def get_username(self,obj):
    #     return str(self.user.username)    

class ShoppingUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def save(self, **kwargs):
        print('deneme')
        return True