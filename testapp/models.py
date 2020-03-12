from django.db import models



class TestEntity(models.Model):

    name        = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class MyModel(models.Model):

    title       = models.CharField(max_length=40)

    def __str__(self):
        return self.title
