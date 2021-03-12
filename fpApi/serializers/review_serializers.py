from rest_framework import serializers
from fpApi.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'rating', 'comment', 'menu_item_id')
        depth = 2


class ReviewSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'rating', 'comment', 'menu_item_id')
