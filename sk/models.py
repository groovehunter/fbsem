from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta


def default_start_time(tdelta):
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    limit = start + timedelta(days=tdelta)
    #if start > now:
    #else:
    #    limit = start + timedelta(days=1)
    return limit


def default_vote_time():
    return default_start_time(14)

def default_suggest_time():
    return default_start_time(7)


class Topic(models.Model):

    question =      models.CharField(max_length=255)
    description =   models.TextField(blank=True)
    #suggestions =   models.ForeignKey(Suggestion, blank=True, null=True, on_delete=models.CASCADE)
    author =        models.ManyToManyField(get_user_model())
    dt_added =      models.DateTimeField(auto_now_add=True)
    dt_updated =    models.DateTimeField(auto_now_add=True)
    suggest_until   = models.DateTimeField(blank=True, default=default_suggest_time)
    vote_until      = models.DateTimeField(blank=True, default=default_vote_time)

    def __str__(self):
        return self.question


class Suggestion(models.Model):

    title =         models.CharField(max_length=255)
    description =   models.TextField(blank=True)
    topic =         models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    dt_added =      models.DateTimeField(auto_now_add=True)
    author =        models.ManyToManyField(get_user_model())
    #    votings =       models.OneToManyField(Voting, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Voting(models.Model):
    suggestion =    models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    person =        models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    vote =          models.IntegerField()
    dt_voted =      models.DateTimeField(auto_now_add=True)
    dt_updated =    models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' %(self.person, self.suggestion, self.vote)
