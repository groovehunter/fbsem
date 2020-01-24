from fbsem.Controller import Controller

from .models import Category
import wikipediaapi

from django import forms



class TermRessource:

    def collect(self, term):

        wiki = wikipediaapi.Wikipedia('de')
        term_cat = "Kategorie:"+term
        cat = wiki.page(term_cat)
        #print_categorymembers(cat.categorymembers)
        subcats = cat.categorymembers
        res = [cat.replace('Kategorie:', '') for cat in subcats]
        return res



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']


#class CategoryForm(forms.Form):
#    cat_name = forms.CharField(label='Kategorien-name', max_length=60)


class CategoryController(Controller, TermRessource):

    def __init__(self, request):
        Controller.__init__(self, request)

    def index(self):
        cat_list = Category.objects.all()

        self.template = 'categories/index.html'
        return self.render()

    def get_name(self):
        # if this is a POST request we need to process the form data
        if self.request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = CategoryForm(self.request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                cat_name = self.request.POST['cat_name']

                return self.redirect('/cat/index')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CategoryForm()

        self.context['form'] = form
        self.template = 'categories/cat_form.html'
        return self.render()



    def import_cat(self):
        """ import categories form """
        term = "Kunst und Kultur"
        subcats = self.collect(term)
        self.context['cat_list'] = subcats
        self.template = 'categories/import.html'
        return self.render()

    def import_process(self):
        """ process import from form """
        self.lg.debug('import_process')
        POST = self.request.POST
        #self.lg.debug(POST)
        parent_name = POST['parent']
        cat_list = POST.getlist('import_sel')
#        self.lg.debug(cat_list)
        #parent_cat = None
        try:
            parent_cat = Category.objects.get(cat_name='root')
        except:
            parent_cat = Category(cat_name='root')
            parent_cat.save()
            #pass

        if parent_name:
            try:
                parent_cat = Category.objects.get(cat_name=parent_name)
            except:
                pass

        for val in cat_list:
            #self.lg.debug('cat import check %s', val)
            try:
                cat = Category.objects.get(cat_name=val)
                self.lg.debug('cat existed %s', val)

            except:
                cat = Category(cat_name=val)
                cat.parent_cat = parent_cat
                cat.save()

        msg = "successful imported"

        return self.redirect('/cat/import', msg=msg)
