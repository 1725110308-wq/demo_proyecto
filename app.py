import web

urls = (
    '/', 'controllers.index.Index',
    '/ver_proveedores', 'controllers.proveedores.ver_proveedores.VerProveedores'
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()