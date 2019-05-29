from django.shortcuts import render,redirect
from .forms import ProfileForm,BusinessForm
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
        return redirect("profile")
    else:

        form=ProfileForm()

    title="Edit"
    return render(request,'edit.html',{'form':form,'title':title})

def business(request):
    if request.method=='POST':
        form=BusinessForm(request.POST)
        if form.is_valid():
            busi=form.save(commit=False)
            busi.user=request.user
            form.save()
        return redirect('profile')

    else:
        form=BusinessForm()
    return render(request,'business.html',{'form':form})
