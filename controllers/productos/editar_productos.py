import web 
import sqlite3
render = web.template.render('views/productos', base='layout')
class EditarProducto:
    def editarProducto(self,producto:dict)->bool:
        try:
            conexion = sqlite3.connect('sql/ferreteriakory.db')
            conexion.row_factory=sqlite3.Row
            cursor = conexion.cursor()
            id_productos = producto['id_productos']
            precio = producto['precio']
            cantidad = producto['cantidad']
            calidad = producto['calidad']
            descripcion = producto['descripcion']
            query = """UPDATE productos
                    SET precio=?,
                        cantidad=?,
                        calidad=?,
                        descripcion=?
                        WHERE id_productos=?"""
            datos=(precio,cantidad,calidad,descripcion,id_productos)
            cursor.execute(query,datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"Error 21: {error.args}")
            return False
        except Exception as errror:
            print(f"Error 22: {errror.args}")
            return False
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
    def POST(self, id_producto):
        formulario=web.input()
        producto={
            "id_productos":formulario['id_productos'],
            "precio":formulario['precio'],
            "cantidad":formulario['cantidad'],
            "calidad":formulario['calidad'],
            "descripcion":formulario['descripcion']
        }
        self.editarProducto(producto)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_productos')
        return ''