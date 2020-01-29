from django.urls import path, include

from . import views
from .views import PersonView, PersonListView

urlpatterns = [
    path('person/', views.p_index),
    path('pgroups/',  views.pg_index),
    path('pl', PersonListView.as_view()),
    path('', views.index),
    path('p', PersonView.as_view()),
]
