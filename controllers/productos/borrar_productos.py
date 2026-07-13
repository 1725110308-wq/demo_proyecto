import web
import sqlite3

render = web.template.render('views/productos')

class BorrarProducto:
    def GET(self):
        return render.borrar_productos()