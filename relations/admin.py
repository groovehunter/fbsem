from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Person, PeopleGroup

#admin.site.register(Person)
#admin.site.register(PeopleGroup)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass
@admin.register(PeopleGroup)
class PeopleGroupAdmin(ImportExportModelAdmin):
    pass
