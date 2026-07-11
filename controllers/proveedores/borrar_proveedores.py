import web
import sqlite3
render = web.template.render('views/proveedores', base='layout')

class BorrarProveedores:
    def borrarProveedor(self,proveedor)->bool:
        try:
            conexion=sqlite3.connect("sql/ferretariasaul.db")
            conexion.row_factory=sqlite3.Row
            cursor=conexion.cursor()
            id_proveedor=proveedor
            query="""DELETE FROM proveedores
                     where id_proveedor=?;"""
            cursor.execute(query,(id_proveedor),)
            conexion.commit()
            conexion.close
            return True
        except sqlite3.Error as error:
            print(f"ERROR 5: {error.args}")
            return False
        except Exception as errror:
            print(f"ERROR 6: {errror.args}")
            return False

    def mostrarPoveedor(self,id_provedor):
        try:
            conexion = sqlite3.connect("sql/ferretariasaul.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM proveedores where id_proveedor = ?;"
            cursor.execute(query,(id_provedor,))
            resultado = cursor.fetchone()

            proveedor = {
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
            print(f"ERROR 3: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 4: {error.args}")
            return {}
        
    def GET(self, id_proveedor:int):
        print(f"id del proveedor: {id_proveedor}")
        proveedor = self.mostrarPoveedor(id_proveedor)
        return render.borrar_proveedores(proveedor)
    
    def POST(self,id_proveedor:int):
        formulario=web.input()
        proveedor=formulario['id_proveedor']
        resultado=self.borrarProveedor(proveedor)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_proveedores')
        return''