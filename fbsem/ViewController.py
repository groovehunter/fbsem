from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from fbsem.settings import BASE_DIR, TMPPATH
from .BaseCtrl import BaseCtrl

import logging


class ViewControllerSupport(BaseCtrl):
    """ schlanke ctrl methods to support django generic views """

    def init_ctrl(self):
        self.context = {}
        self.msg = ''
        self.context['logged_in'] = True
        self.context['prefix_static'] = '/static/'
        self.context['common_static'] = '/static/'
        self.yaml_load()
        self.yamlmenu()

        if self.request.GET:
            GET = self.request.GET
            if 'msg' in GET:
                self.context['msg'] = GET['msg']


    def render(self):
        t = loader.get_template(self.template_name)
        if self.msg:
            self.context['msg'] = self.msg
        html = t.render(self.context, request=self.request)
        response = HttpResponse( )
        response.write(html)
        return response

    def init_logging(self):
        self.lg = logging.getLogger('test')
