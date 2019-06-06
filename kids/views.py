from django.shortcuts import render,redirect
from django.http import HttpRequest,Http404
from .models import KidsClub,KidsCorner,Profile
# Create your views here.

def home(request):
  title='Kids-Vibe'
  return render (request,'home.html',{"title":title})

def gallery(request):
  venues=KidsCorner.objects.all()
  return render(request,'gallery.html',{"venues":venues})

def user_profile(request):
  current_user=request.user 
  profiles = Profile.objects.filter(user=current_user)[0:1]

  return render(request,'profile.html',{"profiles":profiles})