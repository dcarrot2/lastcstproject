from django.conf.urls import patterns, url

from polls import views

#use regular expressions to match anything before /polls and so forth

urlpatterns = patterns('',
    #Show polls                 
    url(r'^$', views.index, name='index'),
                       
    # ex: /polls/5/
    #Voting page
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
                       
    # ex: /polls/5/results/
    #page for results
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
                       
    # ex: /polls/5/vote/
    #page that receives results and stores vote and name into database
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                       
    #ex: /map/
    #page for map
    url(r'^map/$', views.maps, name = 'map'),
                       
    #ex:/polls/5/sendandroid
    #page to encode number of votes per country into json
    url(r'^(?P<poll_id>\d+)/sendandroid/$', views.sendandroid, name='sendandroid'),
                       
    #ex:/polls/5/sendandroidnames
    #page to send names and country they voted for
    url(r'^(?P<poll_id>\d+)/sendandroidnames/$', views.sendandroidnames, name='sendandroidnames'),
                       
    #ex: /polls/5/voteandroid
    #page to receive json objects
    url(r'^(?P<poll_id>\d+)/voteandroid/$',views.voteandroid, name="voteandroid"),
                       
)
