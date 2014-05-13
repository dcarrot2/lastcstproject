from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    #ex: /map/
    url(r'^map/$', views.maps, name = 'map'),
    #ex:/polls/5/sendandroid
    url(r'^(?P<poll_id>\d+)/sendandroid/$', views.sendandroid, name='sendandroid'),
    #ex:/polls/5/sendandroidnames
    url(r'^(?P<poll_id>\d+)/sendandroidnames/$', views.sendandroidnames, name='sendandroidnames'),
                       
)
