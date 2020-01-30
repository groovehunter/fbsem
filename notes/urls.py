from django.urls import path, include

from . import views
from .views import NoteListView, NoteDetailView



urlpatterns = [
    path('', views.NoteListView.as_view()),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
]
