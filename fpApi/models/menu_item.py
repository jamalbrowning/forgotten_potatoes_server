from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        "Restaurant", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    price = models.FloatField()
    category = models.CharField(max_length=50)
