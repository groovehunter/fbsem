

from fbsem.Controller import Controller

from .models import Person, PeopleGroup, Player


class RelationsController(Controller):

    def __init__(self, request):
        Controller.__init__(self, request)

    def p_index(self):
        persons = Person.objects.all()
        data = {}
        data['object_list'] = persons
        self.context['data'] = data
        self.template = 'relations/p_index.html'
        return self.render()

    def pg_index(self):
        self.template = 'relations/pg_index.html'
        return self.render()

    def index(self):
        self.template = 'relations/index.html'
        return self.render()

    def pgd(self):  pass
