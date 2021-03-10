from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class Menu(models.Model):
    rest_id = models.ForeignKey("Restaurant", on_delete=CASCADE)
