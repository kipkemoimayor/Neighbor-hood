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
    image=models.ImageField(upload_to='profile/',blank=True)
    neigbor=models.ForeignKey(Neighbour,on_delete=models.CASCADE)
    location=models.CharField(max_length=50,default='set location')
    secondaryEmail=models.CharField(max_length=50,default='@gmail.com')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname
    class Meta:
        pass


class Businesses(models.Model):
    businessesName=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neigbor=models.ForeignKey(Neighbour,on_delete=models.CASCADE)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.businessesName

class Feeds(models.Model):
    image=models.ImageField(upload_to='feeds/',blank=True)
    post=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neigbor=models.ForeignKey(Neighbour,on_delete=models.CASCADE)
