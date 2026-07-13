import web
import sqlite3

render = web.template.render('views/productos',base='layout')

class BorrarProducto:
    def borrarProducto(self,producto)->bool:
        try:
            conexion=sqlite3.connect('sql/ferreteriakory.db')
            conexion.row_factory=sqlite3.Row
            cursor=conexion.cursor()
            id_producto=producto
            query="DELETE FROM productos where id_productos=?;"
            cursor.execute(query,id_producto)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"Error 17: {error.args}")
            return False
        except Exception as errror:
            print(f"Error 18: {errror.args}")
            return False
        
    def mostrarProducto(self,id_productos):
        try:
            conexion=sqlite3.connect('sql/ferreteriakory.db')
            conexion.row_factory=sqlite3.Row
            cursor=conexion.cursor()
            query="SELECT * FROM productos where id_productos=?;"
            cursor.execute(query,id_productos)
            resultado=cursor.fetchone()
            producto={
                "id_productos":resultado['id_productos'],
                "precio":resultado['precio'],
                "cantidad":resultado['cantidad'],
                "calidad":resultado['calidad'],
                "descripcion":resultado['descripcion']
            }
            conexion.close()
            print(producto)
            return producto
        except sqlite3.Error as error:
            print(f"Error 15: {error.args}")
            return {}
        except Exception as errror:
            print(f"Error 16: {errror.args}")
            return {}
        
    def GET(self,id_productos):
        print(f"id del producto {id_productos}")
        productos=self.mostrarProducto(id_productos)
        return render.borrar_productos(productos)
    
    def POST(self,id_productos):
        formulario=web.input()
        producto=formulario['id_productos']
        resultado=self.borrarProducto(producto)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_productos')
        return''