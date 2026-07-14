import web
import sqlite3
render=web.template.render('views/proveedores',base='layout')
class EditProveedor:
    def editProveedor(self, proveedor: dict)-> bool:
        try:
            conexion=sqlite3.connect('sql/ferreteria.db')
            conexion.row_factory=sqlite3.Row
            cursor=conexion.cursor()
            id_proveedor=proveedor['id_proveedor']
            nombre=proveedor['nombre']
            tipo=proveedor['tipo']
            clase=proveedor['clase']
            nombre_neg=proveedor['nombre_neg']
            query="""UPDATE proveedores
            SET nombre=?,
                tipo=?,
                clase=?,
                nombre_neg=?
            where id_proveedor=?;"""
            datos=(
                nombre,
                tipo,
                clase,
                nombre_neg,
                id_proveedor
            )
            cursor.execute(query,datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"Error 11: {error.args}")
            return False
        except Exception as errror:
            print(f"Error 12: {errror.args}")
            return False
    def mostrarProveedor(self,id_proveedor:int):
        try:
            conexion=sqlite3.connect('sql/ferreteria.db')
            conexion.row_factory=sqlite3.Row
            cursor=conexion.cursor()
            query="select * from proveedores where id_proveedor=?"
            cursor.execute(query,id_proveedor)
            resultado=cursor.fetchone()
            proveedor={
                "id_proveedor":resultado[0],
                "nombre":resultado[1],
                "tipo":resultado[2],
                "clase":resultado[3],
                "nombre_neg":resultado[4]
            }
            conexion.close()
            print(proveedor)
            return proveedor
        except sqlite3.Error as error:
            print(f"Error 9: {error.args}")
            return{}
        except Exception as errror:
            print(f"Error 10: {errror.args}")
            return {}
    def GET(self,id_proveedor: int):
        print(f"ID proveedor {id_proveedor}")
        proveedor=self.mostrarProveedor(id_proveedor)
        return render.edit_proveedor(proveedor)
    def POST(self,id_proveedor:int):
        formulario=web.input()
        proveedor={
            "id_proveedor":formulario['id_proveedor'],
            "nombre":formulario['nombre'],
            "tipo":formulario['tipo'],
            "clase":formulario['clase'],
            "nombre_neg":formulario['nombre_neg']
        }
        resultado=self.editProveedor(proveedor)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_proveedores')
        return ''