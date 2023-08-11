CREATE TABLE "autores" (
	"id_autor"	INTEGER,
	"nombre_autor"	TEXT NOT NULL,
	"estado_autor"	INTEGER NOT NULL,
	PRIMARY KEY("id_autor")
)

CREATE TABLE "categorias" (
	"id_categoria"	INTEGER,
	"nombre_categoria"	TEXT NOT NULL,
	"seccion_categoria"	TEXT NOT NULL,
	PRIMARY KEY("id_categoria")
)

CREATE TABLE "libros" (
	"id_libro"	INTEGER,
	"titulo"	TEXT NOT NULL,
	"id_autor"	INTEGER NOT NULL,
	"id_categoria"	INTEGER NOT NULL,
	"anio_edicion"	TEXT NOT NULL,
	"cant_disponible"	INTEGER NOT NULL,
	"estado_libro"	INTEGER,
	PRIMARY KEY("id_libro")
)

CREATE TABLE "prestamos" (
	"id_prestamo"	INTEGER,
	"ci_usuario"	INTEGER NOT NULL,
	"id_libro"	INTEGER NOT NULL,
	"fecha_prestamo"	TEXT NOT NULL,
	"fecha_devolucion"	TEXT,
	"condicion_devuelto"	TEXT,
	"estado_prestamo"	INTEGER NOT NULL,
	PRIMARY KEY("id_prestamo")
)

CREATE TABLE "usuarios" (
	"ci_usuario"	TEXT,
	"nombre_usuario"	TEXT NOT NULL,
	"apellido_usuario"	TEXT NOT NULL,
	"direccion"	TEXT NOT NULL,
	"departamento"	TEXT NOT NULL,
	"telefono"	TEXT,
	"email"	INTEGER,
	"edad"	INTEGER NOT NULL,
	"estado_usuario"	INTEGER NOT NULL,
	PRIMARY KEY("ci_usuario")
)