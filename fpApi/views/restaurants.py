
from rest_framework import viewsets
from fpApi.models import Restaurant
from fpApi.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
