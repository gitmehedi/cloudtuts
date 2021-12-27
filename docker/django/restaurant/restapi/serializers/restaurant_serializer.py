from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from restapi.models import RestaurantModel


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = ('name', 'contact', 'active')
        validators = [
            UniqueTogetherValidator(queryset=RestaurantModel.objects.all(), fields=['name', 'contact'])
        ]
