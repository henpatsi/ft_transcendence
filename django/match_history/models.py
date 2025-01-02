from django.db import models

# Create your models here.
class Match(models.Model):
    winner = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='winner')
    loser = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True, related_name='loser')
    date = models.DateTimeField(auto_now_add=True)
