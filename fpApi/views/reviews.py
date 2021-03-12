from rest_framework import viewsets, filters
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ViewSet
from fpApi.models import Review, review
from fpApi.serializers import ReviewSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class ReviewViewSet(viewsets.ModelViewSet):

    def list(self, request):
        """Handle GET requests to reviews resource
        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        reviews = Review.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        user = self.request.query_params.get('user', None)
        if user is not None:
            reviews = reviews.filter(user__id=user)

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(serializer.data)
    # queryset = Review.objects.all()
    # serializer_class = ReviewSerializer
    # filter_fields = ('user')
