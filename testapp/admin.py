from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import TestEntity, MyModel


@admin.register(TestEntity)
class TestEntityAdmin(ImportExportModelAdmin):
    pass
