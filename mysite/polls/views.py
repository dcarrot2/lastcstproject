from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import Question, Country, Name #import my django models
import json

#import database models to views.py

def index(request):
    
    latest_poll_list = Question.objects.order_by('-pub_date')[:5]
    #store the five latest polls
    
    context = {'latest_poll_list': latest_poll_list}
    #context dictionary to link polls to html
    
    return render(request, 'polls/index.html', context)
    #render index.html with request and context dictionary


def detail(request, poll_id):

    poll = get_object_or_404(Question, pk=poll_id)
    #get Question object
    #if non-existant, return a 404 error message
    
    return render(request, 'polls/detail.html', {'poll':poll})
    #render detail.html with request and dictionary
    

def results(request, poll_id):
    
    poll = get_object_or_404(Question, pk=poll_id)
    #get Question object
    #if non-existant, return a 404 error message
    
    return render(request, 'polls/results.html', {'poll': poll})
    #render results.html with request and dictionary


def vote(request, poll_id):
    p = get_object_or_404(Question, pk=poll_id)

    try:
        selected_choice = p.country_set.get(pk=request.POST['choice'])


        print "Haha",request.POST['choice'], request.POST['name']
    except (KeyError, Country.DoesNotExist):
        # Redisplay the poll voting form.

        print("What happened?")
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        print selected_choice
        r = Name(name = request.POST['name'],vote = selected_choice)
        selected_choice.votes += 1
        selected_choice.save()
        r.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def maps(request):
    poll_list = Question.objects.order_by('-pub_date')[:5]
    
    country_list = Country.objects.all() #get all Country objects and store into a list

    name_list = Name.objects.all()

    print name_list
    context = {'poll_list': poll_list, 'country_list':country_list, 'name_list': name_list,} #context dictionary to use django's template tags in html
    return render(request, 'polls/map.html',context)

def sendandroid(request, poll_id):
    p = get_object_or_404(Question, pk=poll_id)
    q = get_object_or_404(Country, pk=poll_id)
    selected_choice = p.country_set.get(pk='1')
##    name_choice = q.name_set.get(pk='1')
  
##    choices = p.country_set.all()
   
    num= p.country_set.count() # get number of choices
    response_data = {}
    for i in range(num):
        selected_choice = p.country_set.get(pk=i+1)
        response_data[i+1]= (selected_choice.votes)
        
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def sendandroidnames(request, poll_id):
    c = Name.objects.all()
    num = Name.objects.count()
    response_data={}
    for i in range(num):

        Voter=Name.objects.get(pk=i+1)
        country_choice=Name.objects.get(pk=i+1).vote
        response_data[i+1] = str(Voter) + " " + str(country_choice)

    return HttpResponse(json.dumps(response_data), content_type="application/json")
    
