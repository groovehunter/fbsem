

from .Controller import Controller

class PageController(Controller):

    def __init__(self, request):
        Controller.__init__(self, request)

    def home(self):
        self.template = 'fbsem/base.html'
        return self.render()
