from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('show/<cat_id>', views.show),
    path('import', views.import_cat),
    path('import_lookup', views.import_cat),
    path('import_do', views.import_process),
    path('new', views.new),
]
