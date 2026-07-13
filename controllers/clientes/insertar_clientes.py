import web
import sqlite3

render = web.template.render('views/clientes', base='layout')

class InsertCliente:
    def insertCliente(self, cliente:dict) -> bool:
        try:
            conexion = sqlite3.connect('sql/ferreteriajakob.db')
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            nombre = cliente["nombre"]
            primer_apellido = cliente["primer_apellido"]
            segundo_apellido = cliente["segundo_apellido"]
            telefono = cliente["telefono"]
            email = cliente["email"]

            query = """INSERT INTO clientes(nombre, primer_apellido, segundo_apellido, telefono, email)
                       VALUES (?, ?, ?, ?, ?);"""
            datos = (nombre, primer_apellido, segundo_apellido, telefono, email)

            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 7: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 8: {error.args}")
            return False

    def POST(self):
        formulario = web.input()
        cliente = {
            "nombre": formulario['nombre'],
            "primer_apellido": formulario['primer_apellido'],
            "segundo_apellido": formulario['segundo_apellido'],
            "telefono": formulario['telefono'],
            "email": formulario['email']
        }
        resultado = self.insertCliente(cliente)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_clientes')
        return ''

    def GET(self):
        nombre = ""
        primer_apellido = ""
        segundo_apellido = ""
        telefono = ""
        email = ""
        return render.insertar_clientes(nombre, primer_apellido, segundo_apellido, telefono, email)
