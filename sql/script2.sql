create table clientes(
    id_clientes integer primary key AUTOINCREMENT,
    nombre text not null,
    primer_apellido text not null,
    segundo_apellido text not null,
    telefono text not null,
    email text not null
);
create table proveedores(
   id_proveedor integer primary key AUTOINCREMENT,
   nombre text not null,
   tipo text not null,
   clase text not null,
   nombre_neg text not null 
);
create table productos(
    id_productos integer primary key AUTOINCREMENT,
    precio text not null,
    cantidad text not null,
    calidad text not null,
    descripcion text not null
);
insert into clientes(nombre,primer_apellido,segundo_apellido,telefono,email)
values 
('ocho','orvelin','pineda','21234567895','orvi@gmail.com'),
('nueve','santi','gimenez','8541268259','san@gmail.com');
insert into proveedores(nombre,tipo,clase,nombre_neg)
values
('ollla','dgydvujbiu','ehdvcrfv','hgcygh wf'),
('gvuv','hfcverv','ugveujr','jghvchwvc');
insert into productos(precio,cantidad,calidad,descripcion)
values
('650','Muchos','Buena','Tornillo de concreto'),
('450','Muchos','Buena','Tornillo de madera');
select * from clientes;