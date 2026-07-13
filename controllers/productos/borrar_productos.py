import web
import sqlite3

render = web.template.render('views')

class BorrarProducto:
    def GET(self):
        