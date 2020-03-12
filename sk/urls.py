from django.urls import path, re_path
from .views import TopicListView, TopicDetailView
from .views import SuggestionListView

from .views import index



urlpatterns = [
    re_path('$', index, name='index'),
    path('topic/',          TopicListView.as_view(), name='sk_topics'),
    path('topic/<int:pk>',  TopicDetailView.as_view() ),
    path('topic/<int:topic>/suggest/',  SuggestionListView.as_view()),
    path('suggestions/',           SuggestionListView.as_view(), name='sk_suggestions'),
#    path('suggestion/<int:pk>', SuggestionDetailView.as_view()),
]
