from django.db import models
from django.db.models.deletion import CASCADE


class Restaurant(models.Model):
  name = models.CharField(max_length=50)
