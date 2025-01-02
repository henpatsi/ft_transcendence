from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Match(models.Model):
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='winner')
    loser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='loser')
    date = models.DateTimeField(auto_now_add=True)
