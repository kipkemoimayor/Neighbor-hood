from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighbour(models.Model):
    name=models.CharField(max_length=250)
    location=models.CharField(max_length=220)
    occupationCount=models.IntegerField()

    def __str__(self):
        return self.name



class Profile(models.Model):
    fullname=models.CharField(max_length=50)
    neigbor=models.ManyToManyField(Neighbour)
    # secondaryEmail=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname
