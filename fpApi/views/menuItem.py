from rest_framework import viewsets, filters
from fpApi.models import *
from fpApi.serializers import *
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_fields = ('user', "restaurant", "category")

    def list(self, request):
      """Handle GET requests to reviews resource
      Returns:
          Response -- JSON serialized list of games
      """
      # Get all menu-items records from the database
      menu_items = MenuItem.objects.all().order_by("name")

      # Support filtering menu_items by restaurant

      restaurant = self.request.query_params.get('restaurant', None)
      if restaurant is not None:
          menu_items = menu_items.filter(restaurant__id=restaurant)

      serializer = MenuItemSerializer(
          menu_items, many=True, context={'request': request})
      return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = MenuItem.objects.all()
        menu_item = get_object_or_404(queryset, pk=pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data)
