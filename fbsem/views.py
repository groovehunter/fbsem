

from .PageController import PageController

def home(request):
    ctrl = PageController(request)
    return ctrl.home()
