from django.db import models
from django.utils.timezone import now

now_time = now()

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200) #holds the poll question
    pub_date = models.DateTimeField(default=now_time, blank=True) #holds publication date of object

    def __unicode__(self):
        return self.question #return question in unicode, useful for
                            #when running the shell or admin page

class Country(models.Model):
    poll = models.ForeignKey(Question) #many countries to one question (database relationship)
    choice_text = models.CharField(max_length=200) #hold name of country
    
    votes = models.IntegerField(default=0) #hold number of votes for that country

    class Meta:
        ordering = ["poll"]
        verbose_name_plural = "Countries" #for admin page purposes, gets plural of object

    def __unicode__(self):
        return (self.choice_text) #return country name in unicode

        
class Name(models.Model):
    vote = models.ForeignKey(Country) #many names to one country (database relationship)
    name = models.CharField(max_length=200) #store name


    def __unicode__(self):
        return self.name #return unicode of name
