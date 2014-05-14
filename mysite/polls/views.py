from django.shortcuts import render, get_object_or_404 #render html, context dictionaries and get a single object
from django.http import HttpResponse ,HttpResponseRedirect #generate http responses
from django.core.urlresolvers import reverse
from polls.models import Question, Country, Name #import my django models
from django.views.decorators.csrf import csrf_exempt
import json #for json encoding, decoding

#import database models to views.py

##Note: Context dictionaries returned on the responses allow for the use of django's template tags on the html templates
## Template tags allow one to refer to the database models implicitly

def index(request):
    
    latest_poll_list = Question.objects.order_by('-pub_date')[:5]
    #store the five latest polls
    
    context = {'latest_poll_list': latest_poll_list}
    #context dictionary to link poll list to html
    
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
    #get Question object
    #if non-existant, return a 404 error message

    try:
        selected_choice = p.country_set.get(pk=request.POST['choice'])
        #get the country selected by passing in the request POST id of the country


        print "ID:", request.POST['choice'],"Name:", request.POST['name']
        
    except (KeyError, Country.DoesNotExist):
        

        print("What happened?") #Error message

        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        print "Selected Country:",selected_choice

        #Create instance of name by getting the request POST and the country selected
        r = Name(name = request.POST['name'],vote = selected_choice)

        #Increase the selected country's number of votes by one
        selected_choice.votes += 1 
        
        selected_choice.save() #save changes to database
        
        r.save() #save new name to database
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def maps(request):
    
    poll_list = Question.objects.order_by('-pub_date')[:5] #Generate a poll list
    
    country_list = Country.objects.all() #get all Country objects and store into a list

    name_list = Name.objects.all() #get al the Name objects and store into a list

    context = {'poll_list': poll_list, 'country_list':country_list, 'name_list': name_list,} #context dictionary to use django's template tags in html
    return render(request, 'polls/map.html',context)

@csrf_exempt
def voteandroid(request, poll_id):
    p = get_object_or_404(Question)
    print 'Post from Android'

    try:
        print "Request body:", request.body
        data=json.loads(request.body)
        print "Data:", data
        label=data['choice']
        name = data['Name']
        print 'First check'
        print 'Label:' , label
        selected_choice = p.country_set.get(choice_text=label)
        print 'Second check'
        print 'User made choice with country ' + label + ":"
        print selected_choice
    except:
        print 'Exception: Could not parse JSON'

    selected_choice.votes += 1
    selected_choice.save()

    r = Name(name = str(name), vote=selected_choice)
    r.save()

    return HttpResponse('')


def sendandroid(request, poll_id):
    
    p = get_object_or_404(Question, pk=poll_id)#get Question object
    
    selected_choice = p.country_set.get(pk='1')#get the set of Countries for Question ID 1

   
    num= p.country_set.count() # get number of choices
    response_data = {} #dictionary to store json
    
    for i in range(num):
        selected_choice = p.country_set.get(pk=i+1) #get countries with id of index + 1
        response_data[i+1]= (selected_choice.votes) #store into dict the amount of votes that country has
        
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def sendandroidnames(request, poll_id):

    num = Name.objects.count() #count the number of names
    response_data={} #dictionary to store json
    for i in range(num):

        Voter=Name.objects.get(pk=i+1) #name at id subindex of i plus one
        country_choice=Name.objects.get(pk=i+1).vote #get the country the name voted for
        response_data[i+1] = str(Voter) + " " + str(country_choice) #Store name and country next to each other

    return HttpResponse(json.dumps(response_data), content_type="application/json")#Encode json into the page
    
