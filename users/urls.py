from django.urls import path
from .views import SignUpView
from .views import UserProfileDetailView, UserProfileListView
from .views import PlayerDetailView, PlayerListView
from .views import profile_edit


urlpatterns = [
    path('signup/',     SignUpView.as_view(), name='signup'),
    path('user/<int:pk>',   UserProfileDetailView.as_view()),
    path('user/',           UserProfileListView.as_view()),
    path('player/<int:pk>', PlayerDetailView.as_view()),
    path('player/',         PlayerListView.as_view()),
    path('edit/<int:pk>', profile_edit),
]
