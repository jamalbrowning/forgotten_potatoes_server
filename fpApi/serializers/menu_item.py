from rest_framework import serializers
from fpApi.models import *


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', "description", "price", "category")
