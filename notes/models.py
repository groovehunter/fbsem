from django.db import models
#from categories.models import Category
from django.contrib.auth import get_user_model


class Note(models.Model):

    title   = models.CharField(max_length=40)
    body    = models.TextField()
    dt      = models.DateTimeField()
    author  = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
#    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
