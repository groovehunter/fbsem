from fbsem.settings import DEBUG


class GenericFlow:
    def listview_helper(self):
        keys = self.model._meta.get_fields()
        field_names = [k.name for k in keys]
        for f in self.fields_noshow:
            field_names.remove(f)
        (app, modl) = self.model._meta.label.split('.')
        c = {
            'app'   : app.capitalize(),
            'modl'  : modl,
            'keys'  : field_names,
        }
        if DEBUG:
            c['debug'] = True
        return c
