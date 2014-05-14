from django.contrib import admin


from polls.models import Question, Country, Name

#Registering models to admin page to also manipulate there
admin.site.register(Question)
admin.site.register(Country)
admin.site.register(Name)
