import web
import sqlite3

render = web.template.render('views/clientes', base='layout')

class EditarCliente:

    def actualizarCliente(self, cliente: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteriajakob.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            id_cliente = cliente["id_clientes"]
            nombre = cliente["nombre"]
            primer_apellido = cliente["primer_apellido"]
            segundo_apellido = cliente["segundo_apellido"]
            telefono = cliente["telefono"]
            email = cliente["email"]

            query = """UPDATE clientes 
                SET nombre = ?,
                primer_apellido = ?,
                segundo_apellido = ?,
                telefono = ?,
                email = ?
                WHERE id_clientes = ?;
                """
            datos = (
                nombre,
                primer_apellido,
                segundo_apellido,
                telefono,
                email,
                id_cliente
            )
            cursor.execute(query, datos)
            conexion.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 104: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 105: {error.args}")
            return False
        finally:
            conexion.close()

    def mostrarCliente(self, id_cliente: int):
        try:
            conexion = sqlite3.connect("sql/ferreteriajakob.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            
            # Buscamos al cliente por su ID
            query = "SELECT * FROM clientes WHERE id_clientes = ?;"
            cursor.execute(query, (id_cliente,))
            resultado = cursor.fetchone()

            if resultado is None:
                return {}

            cliente = {
                "id_clientes": resultado[0],
                "nombre": resultado[1],
                "primer_apellido": resultado[2],
                "segundo_apellido": resultado[3],
                "telefono": resultado[4],
                "email": resultado[5]
            }
            print(cliente)
            return cliente
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return {}
        finally:
            conexion.close()

    def GET(self, id_cliente: int):
        print(f"id del cliente a editar: {id_cliente}")
        cliente = self.mostrarCliente(id_cliente)
        return render.edit_clientes(cliente)

    def POST(self, id_cliente: int):
        formulario = web.input()
        cliente = {
            "id_clientes": formulario['id_clientes'],
            "nombre": formulario['nombre'],
            "primer_apellido": formulario['primer_apellido'],
            "segundo_apellido": formulario['segundo_apellido'],
            "telefono": formulario['telefono'],
            "email": formulario['email']
        }
        
        self.actualizarCliente(cliente)
        
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_clientes')
        return ''