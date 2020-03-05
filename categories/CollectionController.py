from fbsem.Controller import Controller

from .models import Item

# mnove to ajax ctrl
from django.http import HttpResponse


class CollectionController(Controller):

    def __init__(self, request):
        Controller.__init__(self, request)

    def index(self):
        self.template = 'categories/index.html'
        return self.render()

    def my(self):
        user = self.request.user
        #pl = user.player
        inv = user.inventory

        collections = inv.collections.all()
        self.lg.debug(collections)
        self.context['debug'] = inv
        self.context['collections'] = collections

        self.template = 'categories/coll.html'
        return self.render()

    def add(self):
        post = self.request.POST.copy()
        self.lg.debug(post)
        html = 'okay'
        response = HttpResponse(html)
        return response


#    def coll(self):
#        coll =
