from . models import Profile,Neighbour,Businesses,Feeds
from django import forms


'''
forms here
'''

class ProfileForm(forms.ModelForm):
    class Meta:

        model=Profile
        exclude=['user']
        widgets={
            "neigbor":forms.Select(),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Businesses
        exclude=['user',]

class PostForm(forms.ModelForm):
    class Meta:
        model=Feeds
        exclude=['user','neigbor']

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
        widgets={
            "neigbor":forms.Select(),
        }

class ChangeHood(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user','image','fullname','location','secondaryEmail']
        widgets={
            "neigbor":forms.Select(),
        }
