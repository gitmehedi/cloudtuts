from django.db import models

from .restaurant import RestaurantModel


class FoodMenuModel(models.Model):
    name = models.CharField(max_length=100)
    restaurant_id = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
    price = models.FloatField()
    actve = models.BooleanField(default=True)

    def __str__(self):
        return self.name
