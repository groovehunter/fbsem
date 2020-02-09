from django.urls import path
from .views import TopicListView, TopicDetailView
from .views import SuggestionListView


urlpatterns = [
    path('topic/',          TopicListView.as_view()),
    path('topic/<int:pk>',  TopicDetailView.as_view()),
    path('topic/<int:topic>/suggest/',  SuggestionListView.as_view()),
#    path('suggest/',           SuggestionListView.as_view()),
#    path('suggestion/<int:pk>', SuggestionDetailView.as_view()),
]
