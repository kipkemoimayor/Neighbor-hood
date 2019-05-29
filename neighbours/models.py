from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighbour(models.Model):
    name=models.CharField(max_length=250)
    location=models.CharField(max_length=220)
    occupationCount=models.IntegerField()



class Profile(models.Model):
    fullname=models.CharField(max_length=50)
    neigbor=models.ForeignKey(Neighbour,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
