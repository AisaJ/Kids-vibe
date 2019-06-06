from django.conf.urls import url,include
from . import views

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
  url(r'^gallery/$',views.gallery,name='gallery'),
  url(r'^profile/$',views.user_profile,name='userProfile'),
]