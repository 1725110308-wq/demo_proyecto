import web
import sqlite3

render = web.template.render('views', base='layout')

class ListaClientes:
 

 
    def consultarClientes(self):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM clientes;"  # tabla clientes
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                cliente = {
                    "id_cliente": fila[0],
                    "nombre": fila[1],
                    "primer_apellido": fila[2],
                    "segundo_apellido": fila[3],
                    "email": fila[4],
                    "telefono": fila[5]
                }
                datos.append(cliente)

            conexion.close()
            return datos
        except sqlite3.Error as error:
            print(f"ERROR 200: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 201: {error.args}")
            return []

    def GET(self):
        clientes = self.consultarClientes()
        return render.lista_clientes(clientes)  # plantilla HTML para clientes