from django.db import models
from django.db.models.deletion import CASCADE


class Restaurant(models.Model):
  user = models.ForeignKey("PotatoUser", on_delete=CASCADE,
                             related_name='restaurantReviewers', related_query_name="restaurantReviewer")
  name = models.CharField(max_length=50)

