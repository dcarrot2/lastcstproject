from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

class Country(models.Model):
    poll = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ["poll"]
        verbose_name_plural = "Countries"

    def __unicode__(self):
        return (self.choice_text)
