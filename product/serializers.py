from rest_framework import serializers
from .models import ProdectModel
from category.models import CategotyModel
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategotyModel
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    # owner_full_name = serializers.SerializerMethodField()
    # category_name = serializers.SerializerMethodField()

    class Meta:
        model = ProdectModel
        fields = ['id', 'name', 'price', 'owner', 'category']

    # def get_owner_full_name(self, obj):
    #     return f'{obj.owner.username}'
    
    # def get_category_name(self, obj):
    #     return f'{obj.category.name}'
    