
from .CategoryController import CategoryController
from .CollectionController import CollectionController

#from fbsem.view_helpers import GenericFlow
from django.views.generic import ListView, DetailView, UpdateView
from .models import Item, ItemCollection
from fbsem.ViewController import ViewControllerSupport

#from .forms import ItemUpdateForm, ItemCreationForm

class ItemUpdateView(UpdateView):
    model = Item
    template_name_suffix = '_update_form'
    fields = ('name', 'category')
    success_url = '/cat/item/'



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

def my(request):
    ctrl = CollectionController(request)
    return ctrl.my()

def coll(request):
    ctrl = CollectionController(request)
    return ctrl.coll()


class GenericDetailView(DetailView, ViewControllerSupport):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.fields_noshow = []
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()


class CollectionDetailView(GenericDetailView):
    model = ItemCollection
    template_name = 'fbsem/generic_obj_sublist.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.fields_noshow = ['items']
        self.init_ctrl()
        self.js_list_common = [
            'collect.js',
        ]
        self.do_js_head()
        self.context.update(self.get_context_data())
        self.context['items'] = self.object.items.all()

        return self.render()



class ItemDetailView(DetailView, ViewControllerSupport):
    model = Item
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['url'] = '/cat/item'
        context['url_list'] = '/cat/item/index'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'categories/generic_detail_obj_img.html'
        self.object = self.get_object()
        self.fields_noshow = []
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()


class ItemListView(ListView, ViewControllerSupport):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        context['url'] = '/cat/item'
        context['url_detail'] = '/cat/item'
        context['url_icon'] = 'images/icons'
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.fields_noshow = ['filepath','filename','itemcollection']
        self.init_ctrl()
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()
