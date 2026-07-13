import web
import sqlite3

render = web.template.render('views')

class BorrarProductos:
    
    def borrarProducto(self, producto) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferretariasaul.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            id_producto = producto
            
            query = """DELETE FROM productos WHERE id_producto = ?;"""
            cursor.execute(query, (id_producto,)) 
            conexion.commit()
            conexion.close()
            return True
        
        except sqlite3.Error as error:
            print(f"ERROR 5: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 6: {error.args}")
            return False

    def mostrarProducto(self, id_producto):
        try:
            conexion = sqlite3.connect("sql/ferretariasaul.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            
            query = "SELECT * FROM productos WHERE id_producto = ?;"
            cursor.execute(query, (id_producto,))
            resultado = cursor.fetchone()
            
            if resultado is None:
                return {}
                

            producto = {
                "id_producto": resultado[0],
                "precio": resultado[1],
                "cantidad": resultado[2],
                "calidad": resultado[3],
                "descripcion": resultado[4]
            }
            conexion.close()
            print(producto)
            return producto
        except sqlite3.Error as error:
            print(f"ERROR 3: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 4: {error.args}")
            return {}

    def GET(self, id_producto: int):
        print(f"id del producto: {id_producto}")
        producto = self.mostrarProducto(id_producto)
        return render.borrar_productos(producto)

    def POST(self, id_producto: int):
        formulario = web.input()
        producto = formulario['id_producto']
        self.borrarProducto(producto)
        
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_productos')
        return ''
