from rest_framework import serializers
from fpApi.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'rest_id')
