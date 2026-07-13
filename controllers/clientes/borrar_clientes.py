import web
import sqlite3

render = web.template.render('views/clientes', base='layout')

class BorrarClientes:
    def borrarCliente(self, cliente_id:int) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteriajakob.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = """DELETE FROM clientes WHERE id_clientes = ?;"""
            cursor.execute(query, (cliente_id,))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 5: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 6: {error.args}")
            return False

    def mostrarCliente(self, id_cliente:int):
        try:
            conexion = sqlite3.connect("sql/ferreteriajakob.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM clientes WHERE id_clientes = ?;"
            cursor.execute(query, (id_cliente,))
            resultado = cursor.fetchone()

            cliente = {
                "id_clientes": resultado[0],
                "nombre": resultado[1],
                "primer_apellido": resultado[2],
                "segundo_apellido": resultado[3],
                "telefono": resultado[4],
                "email": resultado[5]
            }

            conexion.close()
            print(cliente)
            return cliente
        except sqlite3.Error as error:
            print(f"ERROR 3: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 4: {error.args}")
            return {}

    def GET(self, id_cliente:int):
        print(f"id del cliente: {id_cliente}")
        cliente = self.mostrarCliente(id_cliente)
        return render.borrar_clientes(cliente)

    def POST(self, id_cliente:int):
        formulario = web.input()
        cliente_id = formulario['id_clientes']
        resultado = self.borrarCliente(cliente_id)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_clientes')
        return ''
