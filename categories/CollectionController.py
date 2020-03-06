from fbsem.Controller import Controller

from .models import Item

# mnove to ajax ctrl
from django.http import HttpResponse


class CollectionController(Controller):

    def __init__(self, request):
        Controller.__init__(self, request)
        self.user = self.request.user


    def index(self):
        self.template = 'categories/index.html'
        return self.render()

    def my(self):
        #pl = user.player
        inv = self.user.inventory

        collections = inv.collections.all()
        self.lg.debug(collections)
        self.context['debug'] = inv
        self.context['collections'] = collections

        self.template = 'categories/coll.html'
        return self.render()

    def add(self):
        post = self.request.POST.copy()
        tid = post.get('tid')
        user = self.request.user
        inv = user.inventory
        #inv.add(tid)
        self.lg.debug(inv)
        html = 'okay'
        response = HttpResponse(html)
        return response


#    def coll(self):
#        coll =
