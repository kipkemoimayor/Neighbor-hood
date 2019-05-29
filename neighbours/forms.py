from . models import Profile,Neighbour
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
