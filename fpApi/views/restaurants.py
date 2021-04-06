
from rest_framework import viewsets
from fpApi import serializers
from fpApi.models import Restaurant
from fpApi.serializers import RestaurantSerializer
from rest_framework.response import Response


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by("name")
    serializer_class = RestaurantSerializer

    def list(self, request):
        """Handle GET requests to reviews resource
        Returns:
            Response -- JSON serialized list of games
        """
        # Get all review records from the database
        restaurants = Restaurant.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/reviews?user=1
        #
        # That URL will retrieve all reviews by user games
        user = self.request.query_params.get('user', None)
        if user is not None:
            restaurants = restaurants.filter(user__id=user)

        serializer = RestaurantSerializer(
            restaurants, many=True, context={'request': request})
        return Response(serializer.data)
