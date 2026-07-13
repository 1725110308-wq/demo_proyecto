import web 
import sqlite3
render = web.template.render('views/productos', base='layout')
class EditarProducto:
    def mostrarProducto(self,id_productos):
        try:
            conexion = sqlite3.connect('sql/ferreteriakory.db')
            conexion.row_factory=sqlite3.Row
            cursor = conexion.cursor()
            query="""SELECT * FROM productos
                    where id_productos=?"""
            cursor.execute(query,id_productos)
            resultado=cursor.fetchone()
            productos={
                "id_productos":resultado[0],
                "precio":resultado[1],
                "cantidad":resultado[2],
                "calidad":resultado[3],
                "descripcion":resultado[4]
            }
            conexion.close()
            print(productos)
            return productos
        except sqlite3.Error as error:
            print(f"Error 19: {error.args}")
            return False
        except Exception as errror:
            print(f"Error 20: {errror.args}")
            return False

    def GET(self, id_productos):
        print(f"ID del producto {id_productos}")
        prodcutos=self.mostrarProducto(id_productos)
        return render.edit_producto(prodcutos)