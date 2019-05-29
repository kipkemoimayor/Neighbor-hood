from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def profile(request):
    if request.method=='POST':
        form=(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.save()
    else:

        form=ProfileForm()
    return render(request,'profile.html',{'form':form})
