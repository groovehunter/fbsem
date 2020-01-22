from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


class Controller:

    def __init__(self, request):
        self.request = request
        self.context = {}
        self.response = HttpResponse( )
        self.msg = ''


    def render(self):
        t = loader.get_template(self.template)
        html = t.render(self.context, request=self.request)
        if self.msg:
            self.context['msg'] = self.msg
        #self.response['Cache-Control'] = 'no-cache'
        self.response.write(html)
        return self.response
