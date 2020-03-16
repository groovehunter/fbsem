from django.shortcuts import render

#from .models import AModel
from .TestController import TestController

def test1(request):
    ctrl = TestController(request)
    return ctrl.test1()

def catmembers(request, cat):
    ctrl = TestController(request)
    return ctrl.categorymembers(cat=cat)

def video(request):
    ctrl = TestController(request)
    return ctrl.video()

def cat(request):
    ctrl = TestController(request)
    return ctrl.cat()
