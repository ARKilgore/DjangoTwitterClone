from django.conf.urls import patterns, url

from twit import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^(?P<twit_id>\d+)/detail/$', views.detail, name='detail'),
                url(r'^tweet$', views.tweet, name='tweet'),
                )