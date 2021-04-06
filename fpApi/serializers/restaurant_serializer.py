from rest_framework import serializers
from fpApi.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('user','id', 'name')
