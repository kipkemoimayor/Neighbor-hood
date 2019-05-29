from . models import Profile
from django.forms import forms


'''
forms here
'''

class ProfileForm(forms.ModelForm):
    model=Profile
    exclude=['user']
    widgets={
        Neighbour:select(),
    }
