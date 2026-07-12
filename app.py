import web

urls = (
    '/css/(.*)', 'Static',
    '/', 'controllers.index.Index',
    '/ver_proveedores', 'controllers.proveedores.ver_proveedores.VerProveedores',
    '/borrar_proveedores/(.*)', 'controllers.proveedores.borrar_proveedores.BorrarProveedores',
    '/insert_proveedor', 'controllers.proveedores.insert_proveedor.InsertProveedor',
    '/ver_productos','controllers.productos.ver_producto.VerProducto'
)

app = web.application(urls, globals())

class Static:
    def GET(self, filename):
        try:
            with open(f'css/{filename}', 'rb') as f:
                web.header('Content-Type', 'text/css')
                return f.read()
        except IOError:
            raise web.notfound()

if __name__ == '__main__':
    app.run()