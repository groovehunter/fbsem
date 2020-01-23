
from .CategoryController import CategoryController


def index(request):
    ctrl = CategoryController(request)
    return ctrl.index()

def show(request):
    ctrl = CategoryController(request)
    return ctrl.show()

def import_cat(request):
    ctrl = CategoryController(request)
    return ctrl.import_cat()
