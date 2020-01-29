from django.contrib import admin

# Register your models here.
from .models import Person, PeopleGroup

admin.site.register(Person)
admin.site.register(PeopleGroup)
