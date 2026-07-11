import web
render = web.template.render('views/proveedores')

class VerProveedores:
    def GET(self):
        return render.ver_proveedores()