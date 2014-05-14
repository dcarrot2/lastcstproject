##The purpose of this script is to populate database with data with need.
##It's a more autonomous process that can immediately populate the database
##in case the database file is deleted or needed to be deleted

#This script crawls a webpage with countries and stores the countries into a list
#

import os


def populate():

    #open a url with a list of countries
    f = urllib2.urlopen('http://www.projectvisa.com/fullcountrylist.asp').read()
    #turn into soup
    soup = BeautifulSoup(f)

    #array to hold list of all countries
    countryList = []

    #run through the soup and find all html tags with a
    for x in soup.findAll('a'):
        #append any text within those tags to the array
        countryList.append(str(''.join(x.findAll(text=True))))

    #The names of countries are located at even indexes. Odd indexes are the
    #continents where they are located. Let's splice and take the odd items out
        
    countryList = countryList[::2]


    #There's trash leftover at the last couple of indexes on the list

    #Index to start iterating backwards
    trashIndex = -1 

    while(trashIndex != -8): #There's eight items we don't need
        countryList.pop(-1) #Pop those items out
        trashIndex = trashIndex - 1 #Subtract index

    countryList.pop(0) #Pop an empty string from the first index of the list
    

    #add question to poll object
    first_poll = add_poll("What country have you always wanted to visit?")


    #Loop through list and make the country strings into country objects
    print "Storing the countries into the database..."
    
    for i in range(0, len(countryList)):
        add_country(question=first_poll,nation=countryList[i],votes=0)

    #print all question objects
    for q in Question.objects.all():
        print str(q)

    #print all country objects filtered under Question object
    for c in Country.objects.filter(poll=first_poll):
        print str(c)


#Create poll objects
def add_poll(question):
    p = Question.objects.get_or_create(question=question)[0]
    return p

#Create country objects
def add_country(question, nation, votes=0): 
    c = Country.objects.get_or_create(poll=question,choice_text=nation, votes=votes)[0]
    return c



if __name__ == '__main__':
    print "Starting polls application script..."
    print "Crawling the web for a list of countries..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    from polls.models import Question, Country #import my models
    import urllib2
    from bs4 import BeautifulSoup
    populate()
     #Call populate function
