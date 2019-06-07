from django import forms
from .models import KidsClub,KidsCorner,Profile

class NewProfileForm(forms.ModelForm):
  class Meta:
    model=Profile
    exclude=['user']

class NewCornerForm(forms.ModelForm):
  class Meta:
    model=KidsCorner
    fields='__all__'

class NewClubForm(forms.ModelForm):
  class Meta:
    model=KidsClub
    exclude=['user']

