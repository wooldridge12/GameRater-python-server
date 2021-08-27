from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Review, Game, Player

class ReviewView(ViewSet):
    


    def list(self, request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(serializer.data)


    def create(self, request):

        player = Player.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        review = Review()
        review.review = request.data["review"]
        review.game_pictures = request.data["gamePictures"]
        review.player = player
        review.game = game

        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'review', 'game_pictures', 'game', 'player')
