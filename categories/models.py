from django.db import models


class Category(models.Model):

    cat_name        = models.CharField(max_length=60)
    parent_cat_id   = models.IntegerField()
