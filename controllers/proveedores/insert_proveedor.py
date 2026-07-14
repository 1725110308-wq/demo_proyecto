import web
import sqlite3
render=web.template.render('views/proveedores',base='layout')
class InsertProveedor:
    def insertProveedor(self,proveedor:dict)->bool:
        try:
            conexion=sqlite3.connect('sql/ferreteria.db')
            conexion.row_factory=sqlite3.Row
            cursor=conexion.cursor()
            nombre=proveedor["nombre"]
            tipo=proveedor["tipo"]
            clase=proveedor["clase"]
            nombre_neg=proveedor["nombre_neg"]
            query="""insert into proveedores(nombre,tipo,clase,nombre_neg)
            values(?,?,?,?);"""
            datos=(
                nombre,
                tipo,
                clase,
                nombre_neg
            )
            cursor.execute(query,datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 7: {error.args}")
            return False
        except Exception as errror:
            print(f"ERROR 8: {errror.args}")
            return False
        
    def POST(self):
        formulario=web.input()
        proveedor={
            "nombre":formulario['nombre'],
            "tipo":formulario['tipo'],
            "clase":formulario['clase'],
            "nombre_neg":formulario['nombre_neg']
        }
        resultado=self.insertProveedor(proveedor)
        web.ctx.status = '303 See Other'
        web.header('Location', '/ver_proveedores')
        return ''

    def GET(self):
        nombre=""
        tipo=""
        clase=""
        nombre_neg=""
        return render.insert_proveedor(nombre,tipo,clase,nombre_neg)