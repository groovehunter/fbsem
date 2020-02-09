from django.urls import path, include

from . import views
from .CategoryListView import CategoryListView
from .views import ItemListView, ItemDetailView, ItemUpdateView



urlpatterns = [
    path('', views.index),
    path('index', CategoryListView.as_view()),
    path('item/index', ItemListView.as_view()),
    path('item/<int:pk>', ItemDetailView.as_view()),
    path('item/<int:pk>/edit', ItemUpdateView.as_view()),
    path('show/<cat_id>', views.show),
    path('import', views.import_cat),
    path('import_lookup', views.import_cat),
    path('import_do', views.import_process),
    path('new', views.new),
]
