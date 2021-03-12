from fpApi.models import menu_item
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey("PotatoUser", on_delete=CASCADE,
                             related_name='reviewers', related_query_name="reviewer")
    rating = models.IntegerField()
    comment = models.TextField()
    menu_item_id = models.ForeignKey("MenuItem", on_delete=CASCADE)
