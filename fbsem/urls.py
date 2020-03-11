
from django.contrib import admin
from django.urls import path, include

#import testapp
from . import views
#import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/',  include('testapp.urls')),
    #path('cat/',   include('categories.urls')),
    path('categories/',   include('categories.urls')),
    path('rel/',   include('relations.urls')),
    path('notes/',   include('notes.urls')),
    path('sk/',   include('sk.urls'), name='sk'),
    #path('login', views.login),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', views.home),

]
