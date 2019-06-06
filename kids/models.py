from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here

class KidsCorner(models.Model):
  venue=models.CharField(max_length=60)
  image=models.ImageField(upload_to='venues/',default='kids.jpeg')
  description=models.TextField()

  def __str__(self):
    return self.venue
  def save_playground(self):
    self.save()

class KidsClub(models.Model):
  name=models.CharField(max_length=60)   
  location=models.CharField(max_length=60)
  interest=HTMLField()
  user=models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  def save_club(self):
    self.save()

class Profile(models.Model):
  name=models.CharField(max_length=60)
  age=models.IntegerField()
  Gender=models.CharField(max_length=50)
  prof_pic=models.ImageField(upload_to='profiles/',default='avatar.png')
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  club=models.ForeignKey(KidsClub,on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  def save_profile(self):
    self.save()