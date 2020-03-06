from django.urls import path, include

from . import views


urlpatterns = [
    path(''. views.index),
    path('index', ActivityListView.as_view()),
    path('withperson/<int:pk>', views.withperson),


]
