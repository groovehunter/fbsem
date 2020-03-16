
from django.contrib import admin
from django.urls import path, include

#import testapp
from . import views
#import views
#path('cat/',   include('categories.urls')),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/',  include('testapp.urls')),
    path('categories/',   include('categories.urls')),
#    path('rel/',   include('relations.urls')),
    path('notes/',   include('notes.urls')),
#    path('sk/',   include('sk.urls'), name='sk'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', views.home),

]

#path('login', views.login),
