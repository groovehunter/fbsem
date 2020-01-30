from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Note
from django.http import HttpResponse
from django.shortcuts import render
from fbsem.Controller import Controller

from fbsem.view_helpers import GenericFlow


class NoteListView(ListView, GenericFlow):
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        context['url'] = '/notes/'
        context['url_detail'] = '/notes/note'
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'relations/generic_list.html'
        self.object_list = self.get_queryset()
        self.fields_noshow = []
        context = self.get_context_data()
        return render(request, template_name, context)


class NoteDetailView(DetailView, GenericFlow):
    model = Note

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['url'] = '/notes/note'
        context['url_list'] = '/notes/'
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'fbsem/generic_detail_obj.html'
        self.object = self.get_object()
        self.fields_noshow = []
        context = self.get_context_data()
        return render(request, template_name, context)
 
