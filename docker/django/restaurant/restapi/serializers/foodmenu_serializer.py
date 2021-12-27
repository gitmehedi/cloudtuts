from rest_framework import serializers

from restapi.models import FoodMenuModel


class FoodMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenuModel
        fields = ('name', 'active')
