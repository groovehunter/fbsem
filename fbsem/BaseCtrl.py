
import yaml
from os.path import join
from fbsem.settings import BASE_DIR, TMPPATH
import logging


class BaseCtrl:
    """ common methods for gui """

    def yaml_load(self):
        c = open(join(BASE_DIR, 'fbsem/menu.yaml'), encoding='utf8').read()
        self.tree = yaml.load(c)

    def yamlmenu(self):
        """ create datastructure for menu rendering in template
            using menu.yaml config file """

        menudata = []

        for section in self.tree:
            #self.lg.debug('section %s', section )
            sec = list(section.values())[0]
            id = sec['id']
            #self.lg.debug('id %s', id )
            #self.lg.debug('sec %s', sec )
            if True:
                menudata.append( sec )
            else:
                cus_sec = {
                    'href'  :sec['href'],
                    'id'    :sec['id'],
                    'name'  :sec['name'],
                    'links' :[],
                }
                self.lg.debug('sec links %s', sec['links'])
                for item in sec['links']:
                    href = item['href']
                    if self.perm[id][href] == True:
                        cus_sec['links'].append(item)
                menudata.append( cus_sec )

        self.context['menudata'] = menudata
#        self.lg.debug('menudata %s', menudata)


    def do_js_head(self):
        """ rename to do_head // add additional js and css links to head """
        js_head = '' # or js_head
        for line in self.js_list_common:
            js_head += '''<script src="%sjs/%s" type="text/javascript"></script>
''' %(self.prefix_static, line)
        for line in self.js_list:
            js_head += '''<script src="%sjs/%s" type="text/javascript"></script>
''' %(self.prefix_static, line)
        self.context['js_head'] = js_head

        css_head = ''
        for line in self.css_list_common:
            css_head += '''<link href="%scss/%s" type="text/css" rel="stylesheet" />
''' %(self.prefix_static, line)
        self.context['css_head'] = css_head


    def init_logging(self):
        self.lg = logging.getLogger('test')
        if not getattr(self.lg, 'handler_set', None):
            fh = logging.handlers.TimedRotatingFileHandler(TMPPATH+'/log/debug.log', when='midnight')
            fmt = '%(module)s,%(lineno)d - %(levelname)s - %(message)s'
            form = logging.Formatter(fmt=fmt)
            fh.setFormatter(form)
            self.lg.addHandler(fh)
            self.lg.setLevel(logging.DEBUG)
        self.handler_set = True
