from django.db import models


class Review(models.Model):
    review = models.CharField(max_length=150)
    game_pictures = models.ImageField(upload_to='reviews/')
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    