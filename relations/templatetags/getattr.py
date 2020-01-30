

from django import template
register = template.Library()

@register.filter
def getattr(obj, att):
    default = 'n/a'
    try:
        return obj.__getattribute__(att)
    except AttributeError:
        try:
            return obj.__dict__.get(att, default)
        except:
            # just a mistake
            if type(obj) == type((1,2,3)):
                return "tuplealarm"
    except:
        return default
