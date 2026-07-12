import web
import sqlite3
render=web.template.render('views/proveedores',base='layout')
class EditProveedor:
    def mostrarProveedor(self,id_proveedor:int):
        try:
            conexion=sqlite3.connect('sql/ferretariasaul.db')
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