from django.contrib import admin

from .models import Note

#admin.site.register(Note)
from import_export.admin import ImportExportModelAdmin

@admin.register(Note)
class NoteAdmin(ImportExportModelAdmin):
    pass
