from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def api_restaurant_list_view(request):
    restaurant = Restaurant.objects.all()
    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {}
        serializer = RestaurantSerializer(data=request.data['params'])
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
def api_menu_list_view(request):
    menu = Menu.objects.all()
    if request.method == 'GET':
        serializer = MenuSerializer(menu,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {}
        serializer = MenuSerializer(data=request.data['params'], many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
