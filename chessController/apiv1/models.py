from django.db import models

class GameOpenings(models.Model):
    openingName = models.CharField(max_length=900)
    games = models.CharField(max_length=900)
    openingEco = models.CharField(max_length=900)
    whiteRating = models.IntegerField()
    blackRating = models.IntegerField()
    winner = models.CharField(max_length=900)
    totalStrength = models.IntegerField()
# end
