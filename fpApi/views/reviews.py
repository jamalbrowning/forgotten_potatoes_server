from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ViewSet
from fpApi.models import Review, review
from fpApi.serializers import ReviewSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def list(self, request, pk=None):
    #     queryset = Review.objects.all()
    #     # review = get_object_or_404(queryset, pk=pk)
    #     serializer = ReviewSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def list(request):

    #     current_user = User.objects.get(user=request.auth.user)
    #     reviews = Review.objects.filter(user=current_user)

    #     json_reviews = ReviewSerializer(
    #         reviews, many=True, context={'request': request})

    #     return Response(json_reviews.data)
