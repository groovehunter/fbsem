from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('show/<cat_id>', views.show),
    path('import', views.import_cat),
]
