from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    name = models.CharField(max_length=200,unique=True)
    contact = models.CharField(max_length=14)
    active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','contact'],name="%(app_label)s_%(class)s_unique")
        ]

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    current_date = models.DateField(default=timezone.now)
    vote_count = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['name','restaurant'],name="%(app_label)s_%(class)s_unique")
        ]

    def __str__(self):
        return self.name

    def restaurant_name(self):
        return self.restaurant.name
