from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from polls.models import Question, Country
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

        print "Haha",request.POST['choice']
    except (KeyError, Country.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def maps(request):
    return render(request, 'polls/map.html',)

        
##    return HttpResponse("You're voting on poll %s." & poll_id)
