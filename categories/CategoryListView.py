from fbsem.view_helpers import GenericFlow
from django.views.generic import ListView, DetailView, TemplateView
from .models import Category
from fbsem.ViewController import ViewControllerSupport
#from django.shortcuts import render


class CategoryListView(ListView, GenericFlow, ViewControllerSupport):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        #context['person_list'] = Person.objects.all()
        context['rowbox'] = True
        context['url'] = '/cat/'
        context['url_detail'] = '/cat/d'
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.fields_noshow = ['category', 'item', 'note',]
        self.init_ctrl()
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()
        #return render(request, template_name, context)
