from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'contact', 'active')
        validators = [
            UniqueTogetherValidator(queryset=Restaurant.objects.all(), fields=['name', 'contact'])
        ]


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer

    class Meta:
        model = Menu
        fields = ('name', 'price', 'current_date', 'restaurant', 'active', 'vote_count')
        validators = [
            UniqueTogetherValidator(queryset=Menu.objects.all(), fields=['name', 'restaurant'])
        ]
