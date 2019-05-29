from . models import Profile,Neighbour,Businesses
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
        exclude=['user','neigbor']
