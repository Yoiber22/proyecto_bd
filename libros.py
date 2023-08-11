from funciones import *

def alta_libros():
    while True:
        id_libro = ultima_clave('libros','id_libro') + 1
        clear()
        print(COLOR_TITULO + 'Alta de Libros\n')
        print(COLOR_FUENTE + 'ID libro: ',id_libro)

        while True:
            titulo = input(COLOR_INPUT + 'Titulo del Libro: ').title()
            if len(titulo) > 0:
                break
            else:
                obligatorio()

        while True:
            try:
                id_autor = int(input(COLOR_INPUT + 'ID de Autor: '))
                existe_autor, autor = existe_clave('autores','id_autor',id_autor)
                if existe_autor:
                    nombre_autor = autor[0][1] 
                    print(COLOR_FUENTE + f'Autor: {nombre_autor}\n')
                    break
                else:
                    print(COLOR_ERROR + 'ID no encontrada.\n')
            except ValueError:
                print(COLOR_ERROR + 'ID invalida.\n')

        while True:
            try:
                id_categoria = int(input(COLOR_INPUT + 'ID de Categoría: '))
                existe_cat, categoria = existe_clave('categorias','id_categoria',id_categoria)
                if existe_cat:
                    nombre_categoria = categoria[0][1]
                    print(COLOR_FUENTE + f'Categoría: {nombre_categoria}\n')
                    break
                else:
                    print(COLOR_ERROR + 'ID no encontrada.\n')
            except ValueError:
                print(COLOR_ERROR + 'ID invalida.\n') 

        while True:
            try:
                anio_edicion = int(input(COLOR_INPUT + 'Año de Edición: '))
                if anio_edicion in range(1500, anio_acual):
                    break
                else:
                    print(COLOR_ERROR + f'\nRango de Edición valido desde 1500 hasta al {anio_acual}')
            except ValueError:
                print(COLOR_ERROR + '\nEl año es numérico.')

        while True:
            try:
                cant_disponible = int(input(COLOR_INPUT + 'Cantidad disponible: '))
                if cant_disponible > 0:
                    break
                else:
                    print(COLOR_ERROR + '\nLa cantidad debe ser mayor a 0')
            except ValueError:
                print(COLOR_ERROR + '\nLa cantidad es numérica.')

        clear()
        print(COLOR_TITULO + 'Libro a agregar')
        print(COLOR_FUENTE + 'ID          : ',id_libro)
        print(COLOR_FUENTE + 'Titulo      : ',titulo)
        print(COLOR_FUENTE + 'Autor       : ',nombre_autor)
        print(COLOR_FUENTE + 'Categoría   : ',nombre_categoria)
        print(COLOR_FUENTE + 'Año Edición : ',anio_edicion)
        print(COLOR_FUENTE + 'Cant Copias : ',cant_disponible)

        if input(COLOR_INPUT + '\nSeguro desea agregar este libro ? (s/n): ').lower() == 's':
            sql = '''INSERT INTO
                        libros (id_libro,titulo,id_autor,id_categoria,anio_edicion,cant_disponible,estado_libro)
                    VALUES
                        (?,?,?,?,?,?,?)'''
            parametros = (id_libro,titulo,id_autor,id_categoria,anio_edicion,cant_disponible,1)
            correr_consulta(sql,parametros)
            print(COLOR_DESTACAR + 'Libro agregado exitosamente')

        if input(COLOR_INPUT + '\n¿Desea agregar otro libro? (s/n): ').lower() != 's':
            break


def baja_libros():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Baja de Libros\n')
            id_baja = int(input(COLOR_INPUT + 'ID de Libro: '))
            existe_libro, datos_libro = existe_clave('libros','id_libro',id_baja)
            if existe_libro:
                titulo = datos_libro[0][1] 
                if datos_libro[0][-1] == 1:
                    print(COLOR_FUENTE + 'Titulo: ',titulo)

                    if input(COLOR_INPUT + '\n¿Seguro desea dar de baja a este libro? (s/n): ').lower() == 's':
                        sql = 'UPDATE libros SET estado_libro = ? WHERE id_libro = ?'
                        parametros = (0,id_baja)
                        correr_consulta(sql,parametros)
                        print(COLOR_DESTACAR + 'Libro dado de baja exitosamente\n')
                else:
                    print(COLOR_ERROR + f'El libro {titulo} ya esta dado de baja.\n')
                
                if input(COLOR_INPUT + '¿Desea dar de baja otro libro? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'ID no encontrado.\n')
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')


def reactivar_libro():
    # Reactivar libro dado de baja (Por borrado lógico)
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Reactivar Libro\n')
            id_reactivar = int(input(COLOR_INPUT + 'ID de libro: '))
            existe_libro, datos_libro = existe_clave('libros','id_libro',id_reactivar)
            if existe_libro: # Si existe el libro
                titulo = datos_libro[0][1] 
                if datos_libro[0][-1] == 0: # Si esta dado de baja
                    print(COLOR_FUENTE + 'Libro: ',titulo)

                    if input(COLOR_INPUT + '\n¿Seguro desea reactivar este libro? (s/n): ').lower() == 's':
                        sql = 'UPDATE libros SET estado_libro = ? WHERE id_libro = ?'
                        parametros = (1,id_reactivar)
                        correr_consulta(sql,parametros)
                        print(COLOR_DESTACAR + 'Libro reactivado exitosamente\n')
                else:
                    print(COLOR_ERROR + f'El libro {titulo} no esta dado de baja.\n')

                if input(COLOR_INPUT + '¿Desea reactivar otro libro? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'Libro no encontrado.\n')
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')


def modificar_libros():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Modificar Libro\n')
            id_modificar = int(input(COLOR_INPUT + 'Id libro: '))
            existe_libro, datos_libro = existe_clave('libros','id_libro',id_modificar)

            if existe_libro:
                _,datos_autor =  existe_clave('autores','id_autor',datos_libro[0][2])
                _,datos_cat   =  existe_clave('categorias','id_categoria',datos_libro[0][3])
                
                clear()
                print(COLOR_TITULO + 'Datos del libro\n')
                print(COLOR_FUENTE + 'ID          : ',datos_libro[0][0])
                print(COLOR_FUENTE + 'Titulo      : ',datos_libro[0][1])
                print(COLOR_FUENTE + 'Autor       : ',datos_autor[0][1])
                print(COLOR_FUENTE + 'Categoría   : ',datos_cat[0][1])
                print(COLOR_FUENTE + 'Año Edición : ',datos_libro[0][4])
                print(COLOR_FUENTE + 'Copias      : ',datos_libro[0][5])

                if input(COLOR_INPUT + '¿Seguro desea modificar este libro? (s/n): ').lower() == 's':
    
                    while True:
                        print(COLOR_TITULO + '\nCampo a modificar\n')
                        print(COLOR_FUENTE + '1. Titulo')
                        print(COLOR_FUENTE + '2. Autor')
                        print(COLOR_FUENTE + '3. Categoría')
                        print(COLOR_FUENTE + '4. Año edicion')
                        print(COLOR_FUENTE + '5. Cantidad disponible')
                        print(COLOR_FUENTE + '0. Salir\n')
                        opcion = int(input(COLOR_INPUT + 'Ingrese campo a modificar: '))

                        if opcion == 0:
                            break
                        
                        elif opcion == 1:        
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar el titulo? (s/n): ').lower() =='s':
                                    nuevo_titulo = input(COLOR_INPUT + 'Nuevo titulo: ').title()
                                    if len(nuevo_titulo) > 0:
                                        sql = 'UPDATE libros SET titulo = ? WHERE id_libro = ?'
                                        parametros = (nuevo_titulo,id_modificar)
                                        correr_consulta(sql,parametros)
                                        print(COLOR_DESTACAR + '\nLibro modificado exitosamente\n')
                                        break
                                    else:
                                        obligatorio()
                                else:
                                    modificar_libros()
                                
                        elif opcion == 2:
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar el autor? (s/n): ').lower() =='s':
                                    try:
                                        nuevo_autor = int(input(COLOR_INPUT + 'Nueva ID de Autor: '))
                                        existe_autor, autor = existe_clave('autores','id_autor',nuevo_autor)
                                        if existe_autor:
                                            nombre_autor = autor[0][1] 
                                            print(COLOR_FUENTE + 'Autor: ',nombre_autor)
                                            sql = 'UPDATE libros SET id_autor = ? WHERE id_libro = ?'
                                            parametros = (nuevo_autor,id_modificar)
                                            correr_consulta(sql,parametros)
                                            print(COLOR_DESTACAR + '\nLibro modificado exitosamente\n')
                                            break
                                        else:
                                            print(COLOR_ERROR + '\nID no encontrada.')
                                    except ValueError:
                                        input(COLOR_ERROR + '\nID invalida.')
                                else:
                                    modificar_libros()

                        elif opcion == 3:
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar la categoria? (s/n): ').lower() =='s':
                                    try:
                                        nueva_categoria = int(input(COLOR_INPUT + 'Nueva ID de Categoría: '))
                                        existe_cat, categoria = existe_clave('categorias','id_categoria',nueva_categoria)
                                        if existe_cat:
                                            nombre_categoria = categoria[0][1]
                                            print(COLOR_FUENTE + 'Categoría: ',nombre_categoria)
                                            sql = 'UPDATE libros SET id_categoria = ? WHERE id_libro = ?'
                                            parametros = (nueva_categoria,id_modificar)
                                            correr_consulta(sql,parametros)
                                            print(COLOR_DESTACAR + '\nLibro modificado exitosamente\n')
                                            break
                                        else:
                                            print(COLOR_ERROR + '\nID no encontrada.')
                                    except ValueError:
                                        input(COLOR_ERROR + '\nID invalida.')
                                else:
                                    modificar_libros() 

                        elif opcion == 4:
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar el año de edicion? (s/n): ').lower() =='s':
                                    try:
                                        nuevo_anio_edicion = int(input(COLOR_INPUT + 'Nuevo Año de Edición: '))
                                        if nuevo_anio_edicion in range(1500, anio_acual):
                                            sql = 'UPDATE libros SET anio_edicion = ? WHERE id_libro = ?'
                                            parametros = (nuevo_anio_edicion,id_modificar)
                                            correr_consulta(sql,parametros)
                                            print(COLOR_DESTACAR + '\nLibro modificado exitosamente\n')
                                            break
                                        else:
                                            print(COLOR_ERROR + f'\nRango de Edición valido desde 1500 hasta al {anio_acual}')
                                    except ValueError:
                                        input(COLOR_ERROR + '\nEl año es numérico.')
                                else:
                                    modificar_libros()

                        elif opcion == 5:
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar la cantidad de copias? (s/n): ').lower() =='s':
                                    try:
                                        nueva_cant_disponible = int(input(COLOR_INPUT + 'Nueva cantidad de copias: '))
                                        if nueva_cant_disponible > 0:
                                            sql = 'UPDATE libros SET cant_disponible = ? WHERE id_libro = ?'
                                            parametros = (nueva_cant_disponible,id_modificar)
                                            correr_consulta(sql,parametros)
                                            print(COLOR_DESTACAR + 'Libro modificado exitosamente\n')
                                            break
                                        else:
                                            print(COLOR_ERROR + 'La cantidad debe ser mayor a 0.\n')
                                    except ValueError:
                                        input(COLOR_ERROR + 'La cantidad es numérica.\n')
                                else:
                                    modificar_libros()

                if input(COLOR_INPUT + '¿Desea modificar  otro libro? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'Libro no encontrado.\n') 
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')


def listado_libros():
    clear()
    print(COLOR_TITULO + 'Listado de Libros\n')
    sql = 'SELECT * FROM libros'
    datos_libros = correr_consulta(sql)
    if datos_libros != None:
        resultado = []
        for datos_libro in datos_libros:
            _,datos_autor = existe_clave('autores','id_autor',datos_libro[2])
            _,datos_cat   = existe_clave('categorias','id_categoria',datos_libro[3])
            id_libro     = datos_libro[0]
            titulo       = datos_libro[1]
            autor        = datos_autor[0][1]
            categoria    = datos_cat[0][1]
            anio_edicion = datos_libro[4]
            copias       = datos_libro[5]
            estado       = datos_libro[-1]
            if estado == 1:
                estado = 'Activo'
            else:
                estado = 'Baja'

            resultado.append([id_libro,titulo,autor,categoria,anio_edicion,copias,estado]) 
        
        print(COLOR_LISTADO + tabulate(resultado, headers=cabezal_libro, tablefmt='orgbiil1', numalign='center'))      
        input(COLOR_INPUT + '\nIngrese Enter para continuar\n')
    else:
        input(COLOR_ERROR + 'No hay libros para mostrar.\n')

def menu_libros():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Menu de Libros\n')
            print(COLOR_FUENTE + '1. Alta de Libros')
            print(COLOR_FUENTE + '2. Baja de Libros')
            print(COLOR_FUENTE + '3. Reactivar Libro')
            print(COLOR_FUENTE + '4. Modificación de Libros')
            print(COLOR_FUENTE + '5. Listado de Libros')
            print(COLOR_FUENTE + '0. Volver al Menu Principal\n') 
            opcion = int(input(COLOR_INPUT + 'Ingrese opcion: ')) 
            if opcion in range(0,6):
                if opcion   == 0: break
                elif opcion == 1: alta_libros()
                elif opcion == 2: baja_libros()
                elif opcion == 3: reactivar_libro()
                elif opcion == 4: modificar_libros()
                elif opcion == 5: listado_libros()
            else:
                input(COLOR_ERROR + 'Opción fuera de rango.\n')
        except ValueError:
            input(COLOR_ERROR + 'Opción invalida.\n')