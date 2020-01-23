from fbsem.Controller import Controller

from .models import Category
import wikipediaapi


class CategoryController(Controller):

    def __init__(self, request):
        Controller.__init__(self, request)

    def index(self):
        cat_list = Category.objects.all()
        self.template = 'categories/index.html'
        return self.render()

    def import_cat(self):
        wiki = wikipediaapi.Wikipedia('de')

        cat = wiki.page("Kategorie:Kunst und Kultur")
        #print_categorymembers(cat.categorymembers)
        debug = cat.categorymembers

        self.context['cat_list'] = cat.categorymembers
        self.template = 'categories/import.html'
        return self.render()
