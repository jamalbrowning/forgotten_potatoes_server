
from rest_framework import viewsets
from fpApi import serializers
from fpApi.models import Restaurant
from fpApi.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by("name")
    serializer_class = RestaurantSerializer
