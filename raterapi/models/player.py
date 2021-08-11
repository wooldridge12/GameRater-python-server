from django.db import models


class Player(models.Model):
    user_name = models.CharField(max_length=100)
    