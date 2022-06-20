from operator import mod
from django.db import models
# Create your models here.


class Orders(models.Model):
    namber = models.IntegerField()
    price = models.IntegerField()
    price_rub = models.IntegerField()
    date = models.CharField(max_length=10)
    
   