from django.db import models
from django.contrib.auth import get_user_model
from categories.models import ItemCollection


class Person(models.Model):

    name        = models.CharField(max_length=40, unique=True)
    first_name  = models.CharField(max_length=20, null=True)
    last_name   = models.CharField(max_length=20, null=True)
    dt_added    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PeopleGroup(models.Model):

    TYPES = (
        ('GL', 'Geistesleben'),
        ('RL', 'Rechtsleben'),
        ('WL', 'Wirtschaftsleben'),
    )
    name    = models.CharField(max_length=80)
    people  = models.ManyToManyField(Person)
    type    = models.CharField(max_length=2, choices=TYPES)
    dt_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
