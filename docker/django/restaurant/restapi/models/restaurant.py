from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=14, default=None)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


