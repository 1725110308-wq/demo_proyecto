import web
import sqlite3

render = web.template.render('views')

class InsertarProductos:
    def insertarproducto(self, productos: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteriakory.db") 
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            precio = productos["precio"]
            cantidad = productos["cantidad"]
            calidad = productos["calidad"]
            descripcion = productos["descripcion"]

            query = """INSERT INTO productos (precio, cantidad, calidad, descripcion)
                       VALUES (?, ?, ?, ?)"""
            datos = (precio, cantidad, calidad, descripcion)

            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True
        
        except sqlite3.Error as error:
            print(f"Error 1: {error.args}")
            return False
        except Exception as errror:
            print(f"Error 2: {errror.args}")
            return False
        
    def GET(self):
        productos = {
            "precio": "",
            "cantidad": "",
            "calidad": "",
            "descripcion": ""
        }
        return render.productos.insertar_producto(productos)

    def POST(self):
        formulario = web.input()
        
        productos = {
            "precio": formulario.get('precio', ''),
            "cantidad": formulario.get('cantidad', ''),
            "calidad": formulario.get('calidad', ''),
            "descripcion": formulario.get('descripcion', '')
        }

        resultado = self.insertarproducto(productos)
        
        raise web.seeother('/ver_productos')
