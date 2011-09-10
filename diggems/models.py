from django.db import models
from game_helpers import delete_channel

class Player(models.Model):
    channel = models.CharField(max_length=22, unique=True)
    has_bomb = models.BooleanField(default=True)
    last_seen = models.DateTimeField(auto_now=True)
    def delete(self, *args, **kwargs):
        delete_channel(self.channel)
        super(Player, self).delete(*args, **kwargs)

class Game(models.Model):
    mine = models.CharField(max_length=256)
    state = models.SmallIntegerField(default=0)
    token = models.CharField(max_length=22)
    p1 = models.OneToOneField(Player, blank=True, null=True, related_name='game_as_p1')
    p2 = models.OneToOneField(Player, blank=True, null=True, related_name='game_as_p2')
