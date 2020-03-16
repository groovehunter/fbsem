
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.test1),
    path('test1/', views.test1),
    path('cat/', views.cat),

    path('video/', views.video),
    path('cat/<cat>', views.catmembers),
    re_path('cat/$', views.catmembers),
#    re_path('cat/$'), views.cmform),
]
