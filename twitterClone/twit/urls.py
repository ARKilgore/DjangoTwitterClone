from django.conf.urls import patterns, url

from twit import views

urlpatterns = patterns('',
<<<<<<< HEAD
                url(r'^', views.index, name='index'),
                url(r'^(?P<twit_id>\d+)/$', views.detail, name='detail'),
=======
                url(r'^$', views.index, name='index'),
                url(r'^(?P<twit_id>\d+)/detail/$', views.detail, name='detail'),
>>>>>>> FETCH_HEAD
                url(r'^(?P<twit_text>\d+)/(?P<twit_name>\d+)/tweet/$', views.tweet, name='tweet'),
                )