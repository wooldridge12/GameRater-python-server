from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Game, Player, Category

class GameView(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def create(self, request):

        player = Player.objects.get(user=request.auth.user)

        category = Category.objects.get(pk = request.data["category"])

        game = Game()
        game.title = request.data["title"]
        game.player = player
        game.designer = request.data["designer"]
        game.description = request.data["description"]
        game.year_released = request.data["yearReleased"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.estimated_time_to_play = request.data["estimatedTimeToPlay"]
        game.age_recommended = request.data["ageRecommended"]
        game.category = category

        # category = Category.objects.get(pk=request.data["categoryId"])


        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def list(self, request):
        games = Game.objects.all()

        serializer = GameSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'estimated_time_to_play', 'age_recommended', 'category')
        depth = 1
        