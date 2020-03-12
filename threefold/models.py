from django.db import models

from datetime import datetime

class ThreeFoldCategory(models.Model):

    cat_name        = models.CharField(max_length=60, unique=True)
    parent_cat      = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    dt_added        = models.DateTimeField(auto_now_add=True)
#    dt_added

    def __str__(self):
        return self.cat_name



class Item(models.Model):

    name            = models.CharField(max_length=60, unique=True)
    #category        = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE)
    dt_added        = models.DateTimeField(auto_now_add=True)
    filepath        = models.CharField(max_length=255, default='')
    filename        = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name
    def get_img_url(self):
        return 'images/icons/%s200x200/%s' %(self.filepath, self.filename)


class ItemCollection(models.Model):
    name    = models.CharField(max_length=40, unique=True)
    items   = models.ManyToManyField(Item)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/cat/coll/' + str(self.id)


class Inventory(models.Model):
    title       = models.CharField(max_length=40)
#    user       = models.OneToOneField(CustomUser)
    collections = models.ManyToManyField(ItemCollection)

    def __str__(self):
        return self.title
