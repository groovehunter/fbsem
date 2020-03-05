
from django.contrib.auth.models import AbstractUser
from django.db import models
from relations.models import Person
from categories.models import ItemCollection, Inventory


class Player(models.Model):
    name        = models.CharField(max_length=40, unique=True)
    #    user        = models.OneToOneField(get_user_model(), default=None, on_delete=models.CASCADE)
#    collections = models.ManyToManyField(ItemCollection, default=None)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    username    = models.CharField(max_length=40, unique=True)
    person      = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)
    dt_added    = models.DateTimeField(auto_now_add=True)
    player      = models.OneToOneField(Player, on_delete=models.CASCADE, null=True)
#    collections = models.ForeignKey()
    inventory   = models.OneToOneField(Inventory, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
