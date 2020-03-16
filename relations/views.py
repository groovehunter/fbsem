

from .RelationsController import RelationsController
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person, PeopleGroup
from django.http import HttpResponse
from django.shortcuts import render
from fbsem.Controller import Controller
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from fbsem.ViewController import ViewControllerSupport


class PersonView(TemplateView):
    template_name = 'relations/about.html'
    #model = Person

# XXX remove GenericFlow , use ViewControllerSupport
class PersonListView(ListView, ViewControllerSupport):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        #context['person_list'] = Person.objects.all()
        context['rowbox'] = True
        context['url'] = '/rel/pl'
        context['url_detail'] = '/rel/pd'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'relations/person_list.html'
        self.object_list = self.get_queryset()
        self.fields_noshow = ['peoplegroup']
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()



class PeopleGroupListView(ListView, ViewControllerSupport):
    model = PeopleGroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        context['url'] = '/rel/pgl'
        context['url_detail'] = '/rel/pgd'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'relations/generic_list.html'
        self.object_list = self.get_queryset()
        self.fields_noshow = ['people']
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()


class PersonDetailView(DetailView, ViewControllerSupport):
    model = Person
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['url'] = '/rel/pd'
        context['url_list'] = '/rel/pl'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'fbsem/generic_detail_obj.html'
        self.object = self.get_object()
        self.fields_noshow = ['peoplegroup']
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()

class PeopleGroupDetailView(DetailView, ViewControllerSupport):
    model = PeopleGroup
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['url'] = '/rel/pgd'
        context['url_list'] = '/rel/pgl'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'fbsem/generic_detail_obj.html'
        self.object = self.get_object()
        self.fields_noshow = ['people']
        sef.context.update(self.get_context_data())
        return self.render()

#### wow

def pg_index(request):
    ctrl = RelationsController(request)
    return ctrl.pg_index()

def p_index(request):
    ctrl = RelationsController(request)
    return ctrl.p_index()

def index(request):
    ctrl = RelationsController(request)
    return ctrl.index()
