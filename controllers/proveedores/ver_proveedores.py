import web
render = web.template.render('views/proveedores',base='layout')

class VerProveedores:
    def GET(self):
        return render.ver_proveedores()