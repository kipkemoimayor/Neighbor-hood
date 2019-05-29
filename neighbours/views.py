from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def profile(request):
    form=ProfileForm()
    return render(request,'profile.html')
