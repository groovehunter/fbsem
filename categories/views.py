
from .CategoryController import CategoryController


def index(request):
    ctrl = CategoryController(request)
    return ctrl.index()

def show(request):
    ctrl = CategoryController(request)
    return ctrl.show()

def import_cat(request):
    ctrl = CategoryController(request)
    return ctrl.import_lookup()
    #return ctrl.import_cat()

def import_process(request):
    ctrl = CategoryController(request)
    return ctrl.import_process()

def new(request):
    ctrl = CategoryController(request)
    return ctrl.get_name()
