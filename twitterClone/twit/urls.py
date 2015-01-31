from django.conf.urls import patterns, url

from twit import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^authorize$', views.authorize, name='authorize'),
                url(r'^leave$', views.leave, name='leave'),
                url(r'^register$', views.register, name='register'),
                url(r'^signup$', views.signup, name='signup'),
                url(r'^feed$', views.home, name='feed'),
                url(r'^(?P<twit_id>\d+)/detail/$', views.detail, name='detail'),
                url(r'^tweet$', views.tweet, name='tweet'),
                )