from django.shortcuts import render,redirect
from .forms import ProfileForm,BusinessForm,PostForm
from .models import Profile,Businesses,Neighbour
from django.http import HttpResponse

# Create your views here.
def index(request):
    profile=Profile.objects.filter(user_id=request.user.id)
    return render(request,'index.html',{'profile':profile})

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

def feeds(request):

    try:
        profile=Profile.objects.filter(user=request.user)
        arr=[]
        for i in profile:
            arr.append(i.neigbor.id)

        id=arr[0]
        business=Businesses.objects.filter(neigbor=id)
    except Exception as e:
        raise  Http404()

    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.neigbor=Neighbour(id)
            post.save()
        return redirect('feeds')
    else:
        form=PostForm()

    return render(request,"feeds.html",{"business":business,'form':form})
