from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Suggestion, Topic

@admin.register(Suggestion)
class SuggestionAdmin(ImportExportModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    pass
