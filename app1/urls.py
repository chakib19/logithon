from django.conf.urls import url, include 
from . import views

urlpatterns = [
 url(r'^$', views.attaque, name='attaque'),
 url(r'^incident', views.attaque, name='incident'),
 url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
 url(r'^user_create/$',views.attaque_create, name='create'),
 url(r'^attaque_update/(\d+)/$',views.attaque_update, name='update'),
 url(r'^detaille/(?P<id>\d+)/$', views.detaille, name='detaille')
];