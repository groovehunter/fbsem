from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from fbsem.ViewController import ViewControllerSupport
from .models import Activity


#def index(request):
#    return render()


class ActivityListView(ListView, ViewControllerSupport):
    model = Activity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        context['url'] = '/activity/'
        context['url_detail'] = '/activity/'
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.fields_noshow = []
        self.init_ctrl()
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()
