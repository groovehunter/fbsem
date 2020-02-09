from django.contrib.auth import get_user_model
from fbsem.ViewController import ViewControllerSupport
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from django import forms

from users.models import CustomUser
from .models import Topic, Suggestion



class SuggestionListView(ListView, ViewControllerSupport):
    model = Suggestion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        return context

    def get(self, request, *args, **kwargs):
        self.init_ctrl()
        self.object_list = self.get_queryset().filter(**kwargs)
#        self.object_list = self.get_queryset()
        self.fields_noshow = []
        self.lg.debug('kwargs', kwargs['topic'])
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()


class TopicListView(ListView, ViewControllerSupport):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.fields_noshow = ['author']
        self.init_ctrl()
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()


class TopicDetailView(DetailView, ViewControllerSupport):
    model = Topic
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'fbsem/generic_detail_obj.html'
        self.object = self.get_object()
        self.fields_noshow = []
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()
