import web
import sqlite3

render = web.template.render('views')

class VerProducto:
    def verproducto(self,id_productos:int):
        try:
            conexion = sqlite3.connect("sql/ferreteria1.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM ferreteria1 WHERE id_productos = ?"
            cursor.execute(query,(id_productos,))
            resultado = cursor.fetchone()

            productos = {
                "id_productos":resultado[0],
                "precio":resultado[1],
                "cantidad":resultado[2],
                "calidad":resultado[3],
                "descripcion":resultado[4],
            }
            conexion.close()
            print(productos)
            return productos
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return {}

    def GET(self,id_productos:int):
        print(f"ID_CONTACTO: {id_productos}")
        productos = self.verproducto(id_productos)
        return render.ver_productos(productos)