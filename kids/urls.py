from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
  url(r'^gallery/$',views.gallery,name='gallery'),
  url(r'^profile/$',views.user_profile,name='userProfile'),
  url(r'^addProfile/',views.add_profile,name='addProfile'),
]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
