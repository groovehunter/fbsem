from fbsem.Controller import Controller


# mnove to ajax ctrl
from django.http import HttpResponse


class SkController(Controller):

    def __init__(self, request):
        Controller.__init__(self, request)
        self.user = self.request.user


    def index(self):
        self.template = 'sk/index.html'
        return self.render()
