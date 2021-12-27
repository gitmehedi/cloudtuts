from django.db import models
from django.utils import timezone

from .restaurant import Restaurant


class FoodMenu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    current_date = models.DateField(default=timezone.now)
    vote_count = models.IntegerField()
    active = models.BooleanField(default=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
