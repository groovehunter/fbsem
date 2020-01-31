
from .CategoryController import CategoryController

from fbsem.view_helpers import GenericFlow
from django.views.generic import ListView, DetailView
from .models import Item
from fbsem.ViewController import ViewControllerSupport



def index(request):
    ctrl = CategoryController(request)
    return ctrl.index()

def show(request):
    ctrl = CategoryController(request)
    return ctrl.show()

def import_cat(request):
    ctrl = CategoryController(request)
    return ctrl.import_lookup()
    #return ctrl.import_cat()

def import_process(request):
    ctrl = CategoryController(request)
    return ctrl.import_process()

def new(request):
    ctrl = CategoryController(request)
    return ctrl.get_name()



class ItemDetailView(DetailView, GenericFlow, ViewControllerSupport):
    model = Item
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['url'] = '/cat/item'
        context['url_list'] = '/cat/item/index'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'fbsem/generic_detail_obj.html'
        self.object = self.get_object()
        self.fields_noshow = []
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()


class ItemListView(ListView, GenericFlow, ViewControllerSupport):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        context['url'] = '/cat/item'
        context['url_detail'] = '/cat/item/d'
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.fields_noshow = []
        self.init_ctrl()
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()
