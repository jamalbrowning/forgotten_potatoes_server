from rest_framework import serializers
from fpApi.models import *


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id','restaurant', 'name', "description", "price", "category")
        
        depth = 2
