from django.db import models

from relations.models import Person
from datetime import datetime
"""
#FORMAT_STRING = 'TT.MM.JJ HH:mm'
FORMAT_STRING = '%d.%m.%y %H:%M'
class ConvertingDateTimeField(models.DateTimeField):

    def get_prep_value(self, value):
#        if not value:
#        value = '01.03.20 11:00'
        return str(datetime.strptime(value, FORMAT_STRING))
"""


TYPES = {
    ('d', 'Dialed'),
    ('r', 'Received'),
}

class Activity(models.Model):

    title       = models.CharField(max_length=80)
    participant = models.CharField(max_length=50)
    #participant = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=30)
    call_time   = models.DateTimeField()
    call_log    = models.CharField(max_length=1, choices = TYPES)
    duration    = models.TimeField()
    #description = models.TextField()
    #dt_added    = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' %(self.participant, self.call_time)


#class PhoneCall(Activity)
