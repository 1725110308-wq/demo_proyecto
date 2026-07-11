import web
import sqlite3
render = web.template.render('views/proveedores',base='layout')

class VerProveedores:
    def buscarProveedor(self):
        try:
            conexion = sqlite3.connect("sql/ferretariasaul.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM proveedores;"
            cursor.execute(query)
            resultado = cursor.fetchall()
            datos = []
            for fila in resultado:
                proveedor = {
                    "id_proveedor": fila[0],
                    "nombre": fila[1],
                    "tipo": fila[2],
                    "clase": fila[3],
                    "nombre_neg": fila[4]
                }
                datos.append(proveedor)
            conexion.close()
            print(datos)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR 1: {error.args}")
            return {}
        except Exception as errror:
            print(f"ERROR 2: {errror.args}")
            return {}

    def GET(self):
        proveedores = self.buscarProveedor()
        return render.ver_proveedores(proveedores)