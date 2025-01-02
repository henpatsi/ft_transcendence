from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
