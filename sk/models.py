from django.db import models
from django.contrib.auth import get_user_model



class Suggestion(models.Model):

    title =         models.CharField(max_length=255)
    description =   models.TextField(blank=True)
    dt_added =      models.DateTimeField(auto_now_add=True)
    author =        models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.title


class Topic(models.Model):

    question =      models.CharField(max_length=255)
    suggestions =   models.ForeignKey(Suggestion, blank=True, null=True, on_delete=models.CASCADE)
    author =        models.ManyToManyField(get_user_model())
    dt_added =      models.DateTimeField(auto_now_add=True)
    dt_updated =    models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question 
