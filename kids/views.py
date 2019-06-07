from django.shortcuts import render,redirect
from django.http import HttpRequest,Http404
from .models import KidsClub,KidsCorner,Profile,Gallery
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm
# Create your views here.

def home(request):
  title='Kids-Vibe'
  venues=KidsCorner.objects.all()
  return render (request,'home.html',{"title":title,"venues":venues})

def gallery(request):
  gallery=Gallery.objects.all()
  return render(request,'gallery.html',{"gallery":gallery})

def user_profile(request):
  current_user=request.user 
  profiles = Profile.objects.filter(user=current_user)[0:1]

  return render(request,'profile.html',{"profiles":profiles})

@login_required(login_url='/accounts/login')
def add_profile(request):
  current_user=request.user
  if request.method ==  'POST':    
    form = NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      prof_pic=form.cleaned_data['prof_pic']
      name=form.cleaned_data['name']
      gender=form.cleaned_data['gender']
      age=form.cleaned_data['age']
      Profile.objects.filter(user=current_user).update(prof_pic=prof_pic,name=name,gender=gender,age=age)
      profile.save()       
    return redirect('userProfile')

  else:
    form=NewProfileForm()
    return render(request,'new_profile.html',{"form":form})

  