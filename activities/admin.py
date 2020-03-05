from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Activity #, PhoneCall

#admin.site.register(Activity)

@admin.register(Activity)
class ActivityAdmin(ImportExportModelAdmin):
    pass

#@admin.register(PhoneCall)
#class PhoneCallAdmin(ImportExportModelAdmin):#
#    pass
