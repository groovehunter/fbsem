from django.db import models


class Person(models.Model):

    name        = models.CharField(max_length=40, unique=True)
    first_name  = models.CharField(max_length=20, null=True)
    last_name   = models.CharField(max_length=20, null=True)
    dt_added    = models.DateTimeField(auto_now_add=True)


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

class Player(models.Model):
    name        = models.CharField(max_length=40, unique=True)
