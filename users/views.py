
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from fbsem.ViewController import ViewControllerSupport
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django import forms
from users.models import CustomUser, Player
from django.shortcuts import render, get_object_or_404


from .forms import CustomUserCreationForm, CustomUserEditForm, PlayerEditForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile_edit(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        p_form = PlayerEditForm(instance=user.player, data=request.POST)
        u_form = CustomUserEditForm(instance=user, data=request.POST)
    else:
        p_form = PlayerEditForm(instance=user.player)
        u_form = CustomUserEditForm(instance=user)

    template_name = 'users/profile_player.html'
    c = {
            'u_form' : u_form,
            'p_form' : p_form,
        }
    return render(request, template_name, c)

    """
    if not request.POST:
        return render(request, template_name, c)


    if all((p_form.is_valid(), u_form.is_valid())):
        player = p_form.save()
        user = u_form.save(commit=False)
        user.player = player
        user.save()
    """


class UserProfileDetailView(DetailView, ViewControllerSupport):
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['url'] = '/users/profile'
        context['url_list'] = '/users/'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'fbsem/generic_detail_obj.html'
        self.object = self.get_object()
        self.fields_noshow = []
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()


class UserProfileListView(ListView, ViewControllerSupport):
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        context['url'] = '/users/profile/'
        context['url_detail'] = '/user/profile'
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.fields_noshow = ['note', 'Person', 'player']
        if not request.user.is_superuser:
            more = ['password', 'groups', 'user_permissions', 'logentry']
            self.fields_noshow.extend(more)
        self.init_ctrl()
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()

class PlayerListView(ListView, ViewControllerSupport):
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['rowbox'] = True
        context['url'] = '/users/player/'
        context['url_detail'] = '/users/player'
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.fields_noshow = ['']
        self.init_ctrl()
        self.template_name = 'fbsem/generic_list_obj.html'
        self.context.update(self.get_context_data())
        return self.render()

class PlayerDetailView(DetailView, ViewControllerSupport):
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.listview_helper()
        context.update(c)
        context['url'] = '/users/player'
        context['url_list'] = '/users/player/'
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = 'fbsem/generic_detail_obj.html'
        self.object = self.get_object()
        self.fields_noshow = []
        self.init_ctrl()
        self.context.update(self.get_context_data())
        return self.render()
