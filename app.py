import web
urls=(
    '/','controllers.proveedores.ver_proveedores.VerProveedores'
)
app=web.application(urls,globals())
if __name__=='__main__':
    app.run()