from django.core.exceptions import ValidationError
from rest_framework import status, viewsets, filters
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ViewSet
from fpApi import serializers
from fpApi.models import Review, PotatoUser
from fpApi.serializers import ReviewSerializer, ReviewSerializerCreate
from django.contrib.auth.models import User
from rest_framework.response import Response


class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializerCreate
    filter_fields = ('user')
    # def create(self, request):
    #     user = PotatoUser.objects.get(user=request.auth.user)

    #     review = Review
    #     review.user = user
    #     review.rating = request.data["rating"]
    #     review.comment = request.data["comment"]
    #     review.menu_item_id = request.data["menu_item_id"]

    #     try:
    #         review.save()
    #         serializer = ReviewSerializer(review, context={'request': request})
    #         return Response(serializer.data)

    #     except ValidationError as ex:
    #         return Response({"reason": ex.message}, status=status.status.HTTP_400_BAD_REQUEST)

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
