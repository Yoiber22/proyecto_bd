Version de Python 3.10.11

colorama      0.4.6
geographiclib 2.0
geopy         2.3.0
pathlib       1.0.1
pip           23.2.1
setuptools    65.5.0
tabulate      0.9.0

# Motor de Base de Datos (Gestor de Base de Datos)
# Sqlite3 (Base  de Datos Relacional)
# Este, ya viene con Python 3.9 en adelante
# Db Browser for Sqlite (Interfas Grafica para manejar la Base de Datos) 

# Proyeto - Biblioteca 

# Una Biblioteca de la ciudad nos contrata para realizar un control de los libros 
de la biblioteca.
# Dicho control, tendra como finalidad, saber en que condiciones esta un libro dado 
# Los libros, se presentana los usuarios de la biblioteca. Es posible que un libro tenga 
varias copias. (de un libro se tenga varios prestamos simultaneos)
# Para organizar la literatura, los libros estan catalogados en categorias.
# Categorias:
    1. Ciencia
    2. Matematicas
    3. Idiomas
    4. Clasicos 
    5. Cocina
    6. Romanticos
    7. Ficcion
    8. Fantacia
    9. Infantiles

Las catedorias estan en diferentes secciones de la biblioteca: (ubicacion geografica)

ej: Libro: Como aprender cosina Coreana
        Categoria: Cosina
        Seccion: C-4

Datos de los usuarios:
# Cedula de Identidad (elemento identificador)
# Nombre
# Apellido
# Direccion
# Telefono
# e-mail

------------------------------------------------------------------------------------------------------

# Estructurar la informacion proporcinal

- Base de Datos: biblioteca.db

- libros:
id_libro            int PK
tutulo              string Not Null
id_autor            int FK
id_categoria        int FK
anio_edicion        string (fecha) 'aaaa-mm-dd' - sqlite
cant_disponible     int (0, n)
estado_libro        int (1,0) - Borrado logicos -- 1: Acrivo 0: Baja


- Usuarios
cedula              string PK (solo digitos, con un determinado largo, etc)
nombre_usuario      string Not Null
apellido            string Not Null
direccion           string Not Null
telefono            string
email               string
edad                int Not Null
estado_usuario      int (1,0) - Borrado logicos -- 1: Acrivo 0: Baja


- autores
id_autor            int PK
nombre_autor        string Not Null
estado_autor        int (1 - Alta, 0 - Baja)

-- No es posible borrar un autor, si hay libro del mismo

- categorias
id_categoria        int PK
nombre_categoria    string Not Null
seccion_categoria   string Not Null

-- No es posible borrar una categoria, si hay libros en esa categoria

- Prestamos     
id_prestamo         int PK
id_usuario          int FK
id_libro            int FK
fecha_prestamos     string Not Null (aaaa-mm-dd) - fecha del sistema
fecha_devolucion    string
condicion_devuelto  string (Este libro se dio lindo, y vino todo pintado y escrito con hojas rotas)

--------------------------------------------------------------------------------------------------------------

Cuando se realiza un prestamo, cant_disponible de un libro se modifica (-1)
Cuando se devuelva un prestamo, cant_disponible de un libro se modifica (+1)