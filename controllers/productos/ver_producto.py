import web
import sqlite3

render = web.template.render('views')

class VerProducto:
    def GET(self):
        try:
 
            conexion = sqlite3.connect("sql/ferreteriakory.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos;")
            productos = cursor.fetchall()
            conexion.close()
            return render.productos.ver_productos(productos)
            
        except sqlite3.Error as error:
            print(f"Error 102: {error.args}")
            return {}

        except Exception as error:
            print(f"Error 103: {error.args}")
            return {}

