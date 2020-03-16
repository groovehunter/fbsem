
from django import template

register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

@register.simple_tag
def define(the_string):
    return the_string


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
