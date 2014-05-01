from django.contrib import admin

# Register your models here.
from polls.models import Question, Country

admin.site.register(Question)
admin.site.register(Country)
