import web

urls = (
    '/', 'controllers.index.Index',
    '/ver_clientes', 'controllers.clientes.ver_clientes.verclientes',
    '/insertar_clientes', 'controllers.clientes.insertar_clientes.InsertCliente',
    '/borrar_clientes/(.*)', 'controllers.clientes.borrar_clientes.BorrarClientes',
    '/edit_clientes/(.*)', 'controllers.clientes.edit_clientes.EditarCliente',
    '/ver_proveedores', 'controllers.proveedores.ver_proveedores.VerProveedores',
    '/borrar_proveedores/(.*)', 'controllers.proveedores.borrar_proveedores.BorrarProveedores',
    '/insert_proveedor', 'controllers.proveedores.insert_proveedor.InsertProveedor',
    '/ver_productos','controllers.productos.ver_producto.VerProducto',
    '/edit_proveedor/(.*)', 'controllers.proveedores.edit_proveedor.EditProveedor',
    '/insertar_producto', 'controllers.productos.insertar_productos.InsertarProductos',
     '/borrar_productos/(.*)', 'controllers.productos.borrar_productos.BorrarProducto',
     '/edit_producto/(.*)', 'controllers.productos.editar_productos.EditarProducto'
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()