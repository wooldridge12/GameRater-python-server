from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommended = models.IntegerField()
    