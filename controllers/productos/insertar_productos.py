import web
import sqlite3
render=web.template.render('views/productos',base='layout')
class InsertarProductos:
    def insertarProducto(self,producto: dict)->bool:
        try:
            conexion=sqlite3.connect('sql/ferreteriakory.db')
            conexion.row_factory=sqlite3.Row
            cursor=conexion.cursor()
            precio=producto['precio']
            cantidad=producto['cantidad']
            calidad=producto['calidad']
            descripcion=producto['descripcion']
            query="""INSERT INTO productos(precio,cantidad,calidad,descripcion)
                    values(?,?,?,?);"""
            datos=(
                precio,
                cantidad,
                calidad,
                descripcion
            )
            cursor.execute(query,datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 13: {error.args}")
            return False
        except Exception as errror:
            print(f"Error 14: {errror.args}")

    def POST(self):
        formulario=web.input()
        producto={
            "precio":formulario['precio'],
            "cantidad":formulario['precio'],
            "calidad":formulario['calidad'],
            "descripcion":formulario['descripcion']
        }
        resultado=self.insertarProducto(producto)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_productos')
        return ''

    def GET(self):
        precio=""
        cantidad=""
        calidad=""
        descripcion=""
        return render.insertar_producto(precio,cantidad,calidad,descripcion)