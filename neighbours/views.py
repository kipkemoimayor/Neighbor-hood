from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def index(request):
    return render(request,'index.html')

def profile(request):
    profile=Profile.objects.filter(user=request.user)


    return render(request,'profile.html',{'profile':profile})

def edit(request):

    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
    else:

        form=ProfileForm()

    title="Edit"
    return render(request,'edit.html',{'form':form,'title':title})
