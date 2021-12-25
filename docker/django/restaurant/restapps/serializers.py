from rest_framework import serializers

from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'contact', 'active')


class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer
    class Meta:
        model = Menu
        fields = ('name', 'price', 'current_date', 'restaurant', 'active','vote_count')
