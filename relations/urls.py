from django.urls import path, include

from . import views
from .views import PersonView, PersonListView, PersonDetailView, PeopleGroupDetailView, PeopleGroupListView

urlpatterns = [
    path('person/', views.p_index),
    path('pgroups/',  views.pg_index),
    path('pl', PersonListView.as_view()),
    path('pgl', PeopleGroupListView.as_view()),
    path('pd/<int:pk>', PersonDetailView.as_view(), name='pd'),
    path('pgd/<int:pk>', PeopleGroupDetailView.as_view()),
    path('', views.index),
    path('p', PersonView.as_view()),
]
