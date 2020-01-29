

from .RelationsController import RelationsController
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person
from django.http import HttpResponse
from django.shortcuts import render

class PersonView(TemplateView):
    template_name = 'relations/about.html'
    #model = Person

class PersonListView(ListView):
    model = Person

    def head(self, *args, **kwargs):
        last = self.get_queryset().latest('dt_added')
        response = HttpResponse()
        # RFC 1123 date format
        response['Last-Modified'] = last.dt_added.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

    def get(self, request, *args, **kwargs):
        template_name = 'relations/person_list.html'
#        data = self.get_queryset().all().values()
        data = self.get_queryset().all().values_list()
        keys = Person._meta.get_fields()
        field_names = [k.name for k in keys]
        field_names.remove('peoplegroup')
        app = {'name': 'Relations', 'model': 'person'}
        context = {
            'app'   : app,
            'data': data,
            'keys': field_names,
            'rowbox':   True,
            }
        return render(request, template_name, context)
#        response = HttpResponse()
#        return response



class PersonDetail(DetailView):
    model = Person

class PersonCreate(CreateView):
    model = Person

class PersonUpdate(UpdateView):
    model = Person

class PersonDelete(DeleteView):
    model = Person



def pg_index(request):
    ctrl = RelationsController(request)
    return ctrl.pg_index()

def p_index(request):
    ctrl = RelationsController(request)
    return ctrl.p_index()

def index(request):
    ctrl = RelationsController(request)
    return ctrl.index()
