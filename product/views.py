from django.shortcuts import render
from .models import *
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import generics
from .filters import ProductFilter
from django_filters import rest_framework as filters

# Create your views here.


# class ProductModelViewSet(ModelViewSet):
#     queryset = ProdectModel.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = ProductFilter

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = CategotyModel.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategotyModel.objects.all()
    serializer_class = CategorySerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = ProdectModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = ProductFilter
    ordering_fields = ['price']
    ordering = ['price']

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProdectModel.objects.all()
    serializer_class = ProductSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



