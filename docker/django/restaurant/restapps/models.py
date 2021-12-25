from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
