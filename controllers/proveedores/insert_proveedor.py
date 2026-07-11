import web
render=web.template.render('views/proveedores',base='layout')
class InsertProveedor:
    def GET(self):
        return render.insert_proveedor()