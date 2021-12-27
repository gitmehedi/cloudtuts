from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from restapi.models import FoodMenu

from .restaurant_serializer import RestaurantSerializer


class FoodMenuSerializer(serializers.ModelSerializer):
    restaurant_id = RestaurantSerializer

    class Meta:
        model = FoodMenu
        fields = ('name', 'active', 'restaurant_id', 'price', 'current_date', 'vote_count')

        validators = [
            UniqueTogetherValidator(queryset=FoodMenu.objects.all(), fields=['name', 'restaurant_id', 'current_date'])
        ]
