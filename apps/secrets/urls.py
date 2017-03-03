from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^homepage$', views.homepage),
    url(r'^create$', views.create),
    url(r'^popular$', views.popular, name='popular'),
    url(r'^like$', views.like),
    url(r'^delete$', views.delete),
	url(r'^likePop$', views.likePop),
	url(r'^mine$', views.mine),
	url(r'^logout$', views.logout),
]
