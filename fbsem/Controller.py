from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from fbsem.settings import TMPPATH, DEBUG
from .BaseCtrl import BaseCtrl

import logging



class Controller(BaseCtrl):

    def __init__(self, request):
        if DEBUG:
            self.init_logging()
        self.request = request
        self.init_ctrl()

        if request.user.is_authenticated:
            self.init_user_and_inventory()

    def init_ctrl(self):
        self.context = {}
        self.msg = ''
        self.context['logged_in'] = True
        self.context['prefix_static'] = '/static/'
        self.context['common_static'] = '/static/'
        self.yaml_load('menu')
        self.yamlmenu('menu')
        #if self.request.user.is_staff:
        #    self.yaml_load('menu_admin')
        #    self.yamlmenu('menu_admin')
        self.pathargs()


        if self.request.GET:
            GET = self.request.GET
            if 'msg' in GET:
                self.context['msg'] = GET['msg']

    def init_user_and_inventory(self):
        user = self.request.user
#        self.context['inv'] = user.inventory
        #self.lg.debug(user.inventory)


    def render(self):
        t = loader.get_template(self.template)
        html = t.render(self.context, request=self.request)
        if self.msg:
            self.context['msg'] = self.msg
        self.response = HttpResponse( )
        #self.response['Cache-Control'] = 'no-cache'
        self.response.write(html)
        return self.response

    def redirect(self, url, msg=''):
        if msg:
            url = url + '?msg=' + msg
        return HttpResponseRedirect(url)
