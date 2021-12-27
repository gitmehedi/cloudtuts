from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from restapi.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'contact', 'active')
        validators = [
            UniqueTogetherValidator(queryset=Restaurant.objects.all(), fields=['name', 'contact'])
        ]
