from rest_framework import viewsets
from fpApi.models import *
from fpApi.serializers import *


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    depth = 2
