

from .PageController import PageController
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    ctrl = PageController(request)
    return ctrl.home()


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect('/?msg=Login%20erfolgreich')

    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/?msg=Login%20failed')
