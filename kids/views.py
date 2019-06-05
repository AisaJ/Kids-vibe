from django.shortcuts import render
from django.http import HttpRequest,Http404
# Create your views here.

def home(request):
  title='Kids-Vibe'
  return render (request,'home.html',{"title":title})