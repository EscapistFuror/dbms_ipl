from django.conf import settings
from django.db import models


class Team(models.Model):
    TName = models.CharField(max_length=200)
    balance = models.IntegerField()
    player_count = models.IntegerField()
    def __str__(self):
        return self.TName

class Player(models.Model):
    country = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    base_price = models.IntegerField(default=0)
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Sold_Players(models.Model):
    name = models.ForeignKey(Player, on_delete=models.CASCADE)
    bid_price = models.IntegerField()
    TName = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name