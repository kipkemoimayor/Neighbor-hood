from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighbour(models.Model):
    name=models.CharField(max_length=250)
    location=models.CharField(max_length=220)
    occupationCount=models.IntegerField()

    def __str__(self):
        return self.name

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        neigbor=Neighbour.objects.all().delete()
        return neigbor
    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        neigbor=cls.objects.filter(id=neigborhood_id)
        return neigbor





class Profile(models.Model):
    fullname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='profile/',blank=True)
    neigbor=models.ForeignKey(Neighbour,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    secondaryEmail=models.EmailField(max_length=50)
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

    def create_business(self):
        self.save()
    def delete_business(self):
        busines=Businesses.objects.all().delete()
        return busines

    def update_business(self):
        updated=Businesses.objects.filter(id=1).update(businessesName='collo')
        return updated
    @classmethod
    def find_business(cls,business_id):
        busines=cls.objects.filter(id=business_id)
        return busines

    @classmethod
    def search_business(cls,name):
        busines=cls.objects.filter(businessesName__icontains=name)
        return busines


class Feeds(models.Model):
    image=models.ImageField(upload_to='feeds/',blank=True)
    post=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neigbor=models.ForeignKey(Neighbour,on_delete=models.CASCADE)

    def __str__(self):
        return self.post

    def save_post(self):
        self.save()
