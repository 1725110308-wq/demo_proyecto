import web
import sqlite3

render = web.template.render('views/clientes', base='layout')

class verclientes:
    def consultarClientes(self):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM clientes;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                clientes = {
                    "id_clientes": fila[0],
                    "nombre": fila[1],
                    "primer_apellido": fila[2],
                    "segundo_apellido": fila[3],
                    "telefono": fila[4],
                    "email": fila[5]
                }
                datos.append(clientes)

            conexion.close()
            return datos
        except sqlite3.Error as error:
            print(f"ERROR 200: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 201: {error.args}")
            return {}

    def GET(self):
        clientes = self.consultarClientes()
        return render.ver_clientes(clientes)