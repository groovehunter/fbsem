from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category, Item, ItemCollection, Inventory


#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass

@admin.register(ItemCollection)
class ItemCollectionAdmin(ImportExportModelAdmin):
    pass

@admin.register(Inventory)
class InventoryAdmin(ImportExportModelAdmin):
    pass
