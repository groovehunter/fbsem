
from fbsem.Controller import Controller
#import facebook
#import wikipediaapi
from testapp.credentials import *

#graph = facebook.GraphAPI(access_token=access_token, version="2.12")
#graph = facebook.GraphAPI(access_token=user_token, version="2.12")
"""
def print_categorymembers(categorymembers, level=0, max_level=1):
    for c in categorymembers.values():
        print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)
"""


class TestController(Controller):

    def __init__(self, request):
        Controller.__init__(self, request)
        #self.wiki = wikipediaapi.Wikipedia('de')

    def fb(self):
        obj_id = 'SelbstSozialTransformativKunst'
        obj_id = 330999471123244
        #post = graph.get_object(id=obj_id, fields='about')
        #print(post['message'])
        canvas_url = 'http://oo.kosmospora.de/'
        perms = ["manage_pages","publish_pages"]
        #url_login = graph.get_auth_url(app_id, canvas_url, perms)

    def test1(self):
        debug = ''
        self.context['debug'] = debug
        self.context['values'] = debug
        self.template = 'testapp/test1.html'
        return self.render()


    def categorymembers(self, cat=''):
        self.template = 'testapp/catlist.html'
        if not cat:
            return self.render()
        cat = self.wiki.page("Kategorie:"+cat)
#        debug = cat.categorymembers
        self.context['debug'] = debug
        self.context['values'] = debug

        return self.render()

    def error(self):
        debug = 'ERROR'
        self.template = 'testapp/error.html'
