from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from category.serializer import CategorySerializer
from .models import Category

# Create your views here.
class CategoryViewset(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request:Request, pk=None):
        post = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)