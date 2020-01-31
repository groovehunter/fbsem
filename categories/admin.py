from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category, Item

#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass
