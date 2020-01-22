from django.shortcuts import render

from .TestController import TestController

def test1(request):
    ctrl = TestController(request)
    return ctrl.test1()

def catmembers(request, cat):
    ctrl = TestController(request)
    return ctrl.categorymembers(cat=cat)
