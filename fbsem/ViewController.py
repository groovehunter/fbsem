from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from fbsem.settings import BASE_DIR, TMPPATH, DEBUG
from .BaseCtrl import BaseCtrl

#import logging


class ViewControllerSupport(BaseCtrl):
    """ schlanke ctrl methods to support django generic views """

    def init_ctrl(self):
        if DEBUG:
            self.init_logging()
        self.context = {}
        self.msg = ''
        self.context['logged_in'] = True
        self.prefix_static = '/static/'
        self.context['prefix_static'] = self.prefix_static

        self.context['common_static'] = '/static/'
        self.yaml_load('menu')
        self.yamlmenu('menu')
        self.js_list = []
        self.js_list_common = []
        self.css_list_common = []

        if self.request.GET:
            GET = self.request.GET
            if 'msg' in GET:
                self.context['msg'] = GET['msg']


    def listview_helper(self):
        keys = self.model._meta.get_fields()
        field_names = [k.name for k in keys]
        #self.lg.debug('removed fields from display: %s', self.fields_noshow)
        for f in self.fields_noshow:
            if f in field_names:
                field_names.remove(f)
        field_names.remove('id')
        (app, modl) = self.model._meta.label.split('.')
        try:
            url = self.model.get_absolute_url()
        except:
            url = '/{0}/{1}'.format(app,modl.lower())
        url_detail = url
        c = {
            'app'   : app.capitalize(),
            'modl'  : modl,
            'keys'  : field_names,
            'url'   : url,
            'url_detail': url_detail,
        }
        if DEBUG:
            c['debug'] = True
        return c

    def render(self):
        t = loader.get_template(self.template_name)
        if self.msg:
            self.context['msg'] = self.msg
        html = t.render(self.context, request=self.request)
        response = HttpResponse( )
        response.write(html)
        return response
1
