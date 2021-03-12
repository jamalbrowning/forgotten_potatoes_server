from rest_framework import viewsets
from fpApi.models import *
from fpApi.serializers import *


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
