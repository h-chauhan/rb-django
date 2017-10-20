from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def category_list(request):
    objects = Category.objects.all();
    serializer = CategorySerializer(objects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(obj)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    objects = Product.objects.all();
    serializer = ProductSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(obj)
    return Response(serializer.data)

@api_view(['POST'])
def order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
