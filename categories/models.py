from django.db import models

from datetime import datetime

class Category(models.Model):

    cat_name        = models.CharField(max_length=60, unique=True)
    parent_cat      = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    dt_added        = models.DateTimeField(auto_now_add=True)
#    dt_added

    def __str__(self):
        return self.cat_name



class Item(models.Model):

    name            = models.CharField(max_length=60, unique=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    dt_added        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
