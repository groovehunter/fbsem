from django.db import models

from datetime import datetime

class Category(models.Model):

    cat_name        = models.CharField(max_length=60, unique=True)
    parent_cat      = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    dt_added        = models.DateTimeField(auto_now_add=True)
#    dt_added        = models.DateTimeField(auto_now=True, default=datetime.now)
