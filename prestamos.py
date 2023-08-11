from funciones import * 

def ingresar_presatamos():
    while True:
        id_prestamo = ultima_clave('prestamos','id_prestamo') + 1
        fecha_prestamo_bd = fecha_actual.strftime(FORMATO_BD)
        fecha_prestamo = fecha_actual.strftime(FORMATO_FECHA)
        clear()
        print(COLOR_TITULO + 'Ingresar Préstamo\n')
        print(COLOR_FUENTE + 'ID préstamo: ',id_prestamo)

        while True:
            ci_usuario = input(COLOR_INPUT + 'CI usuario: ')
            existe_usuario, datos_usuario = existe_clave('usuarios','ci_usuario',ci_usuario)
            if existe_usuario:
                nombre_usuario = datos_usuario[0][1]
                apellido_usuario = datos_usuario[0][2]
                estado_usuario = datos_usuario[0][-1]
                if estado_usuario == 1:
                    print(COLOR_FUENTE + f'Usuario: {nombre_usuario} {apellido_usuario}')
                    break
                else:
                    print(COLOR_ERROR + 'Usuario dado de baja.\n')
            else:
                print(COLOR_ERROR + 'Usuario no encontrado.\n')

        while True:
            try:
                id_libro = int(input(COLOR_INPUT + '\nID de libro a prestar: '))
                existe_libro, datos_libro = existe_clave('libros','id_libro',id_libro)
                if existe_libro:
                    cant_diponibles = datos_libro[0][5]
                    estado_libro = datos_libro[0][-1]
                    titulo = datos_libro[0][1]
                    id_libro = datos_libro[0][0]
                    if cant_diponibles > 0:
                        if estado_libro == 1:
                            print(COLOR_FUENTE + 'Libro: ',titulo)
                            print(COLOR_FUENTE + 'Cantidad disponible: ',cant_diponibles)
                            break
                        else:
                            print(COLOR_ERROR + 'Libro dado de baja.')
                    else:
                        print(COLOR_ERROR + f'No quedan unidades del libro {titulo}')   
                else:
                    print(COLOR_ERROR + 'Libro no encontrado.')
            except ValueError:
                input(COLOR_ERROR + 'ID inválida.')

        clear()
        print(COLOR_TITULO + 'Préstamo a ingresar')
        print(COLOR_FUENTE + 'ID prestamo : ',id_prestamo)
        print(COLOR_FUENTE + 'Fecha       : ',fecha_prestamo)
        print(COLOR_FUENTE + 'CI          : ',ci_usuario)
        print(COLOR_FUENTE + f'Nombre      :  {nombre_usuario} {apellido_usuario}')
        print(COLOR_FUENTE + 'Libro       : ',titulo)

        if input(COLOR_INPUT + '¿Desea ingresar este prestamo? (s/n): ').lower() == 's':
            sql = '''INSERT INTO
                        prestamos (id_prestamo,ci_usuario,id_libro,fecha_prestamo,estado_prestamo)
                    VALUES
                        (?,?,?,?,?)'''
            parametros = (id_prestamo,ci_usuario,id_libro,fecha_prestamo_bd,1)
            correr_consulta(sql,parametros)

            sql = 'UPDATE libros SET cant_disponible = cant_disponible - 1 WHERE id_libro = ?'
            parametros = (id_libro,)
            correr_consulta(sql,parametros)
            print(COLOR_DESTACAR + 'Préstamo ingresado exitosamente.\n')

        if input(COLOR_INPUT + '¿Desea ingresar otro prestamo? (s/n): ').lower() != 's':
            break


def devoliciones():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Devolución de Libro\n')
            id_devolucion = input(COLOR_INPUT + 'ID Préstamo: ')
            existe_prestamo, datos_prestamo = existe_clave('prestamos','id_prestamo',id_devolucion)
            if existe_prestamo:
                if datos_prestamo[0][-1]:
                    _,datos_usuario  = existe_clave('usuarios','ci_usuario',datos_prestamo[0][1])
                    _,datos_libro    = existe_clave('libros','id_libro',datos_prestamo[0][2])
                    ci_usuario       = datos_usuario[0][0]
                    nombre_usuario   = datos_usuario[0][1]
                    apellido_usuario = datos_usuario[0][2]
                    id_libro         = datos_libro[0][0]
                    titulo_libro     = datos_libro [0][1]
                    fecha_prestamo_dt= datetime.strptime(datos_prestamo[0][3],FORMATO_BD)
                    fecha_prestamo   = fecha_prestamo_dt.strftime(FORMATO_FECHA)
                    fecha_devolucion_bd = fecha_actual.strftime(FORMATO_BD)
                    fecha_devolucion    = fecha_actual.strftime(FORMATO_BD)

                    print(COLOR_FUENTE + f'Usuario: {nombre_usuario} {apellido_usuario}')
                    print(COLOR_FUENTE + f'Libro: {titulo_libro}')
                
                    if input(COLOR_INPUT + '\n¿Desea agregar un comentario sobre la condición del libro? (s/n): ').lower() =='s':
                        condicion_libro = input(COLOR_INPUT + 'Condición del libro: ')
                    else:
                        condicion_libro = 'N/A'

                    clear()
                    print(COLOR_TITULO + 'Devolución de libro\n')
                    print(COLOR_FUENTE + f'Libro            : {titulo_libro}')
                    print(COLOR_FUENTE + f'CI Usuario       : {ci_usuario}')
                    print(COLOR_FUENTE + f'Nombre           : {nombre_usuario} {apellido_usuario}')
                    print(COLOR_FUENTE + f'Fecha prestamo   : {fecha_prestamo}')
                    print(COLOR_FUENTE + f'Fecha devolución : {fecha_devolucion}')
                    print(COLOR_FUENTE + f'Comentario       : {condicion_libro}')

                    if input(COLOR_INPUT + '\nConfirma ingresar la devolucion (s/n): ').lower() == 's':

                        if condicion_libro == 'N/A':
                            condicion_libro = None

                        sql = '''UPDATE 
                                    prestamos
                                SET
                                    fecha_devolucion = ?, condicion_devuelto = ?, estado_prestamo = ?
                                WHERE
                                    id_prestamo = ?'''
                        parametros = (fecha_devolucion_bd,condicion_libro,0,id_devolucion)
                        correr_consulta(sql,parametros)

                        sql = 'UPDATE libros SET cant_disponible = cant_disponible + 1 WHERE id_libro = ?'
                        parametros = (id_libro,)
                        correr_consulta(sql,parametros)

                        print(COLOR_DESTACAR + 'Devolución ingresada exitosamente.\n')

                        if input(COLOR_INPUT + '¿Desea ingresar otra devolucion? (s/n): ').lower() != 's':
                            break
                    else:
                        break
                else:
                    input(COLOR_ERROR + 'Ya fue devuelto.\n')
            else:
                input(COLOR_ERROR + 'Préstamo no encontrado.\n')
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')

def consultar_prestamo():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Consultar Préstamo\n')
            id_consultar = int(input(COLOR_INPUT + 'ID Préstamo: '))
            existe_prestamo, datos_prestamo = existe_clave('prestamos','id_prestamo',id_consultar)
            if existe_prestamo:
                _,datos_usuario  = existe_clave('usuarios','ci_usuario',datos_prestamo[0][1])
                _,datos_libro    = existe_clave('libros','id_libro',datos_prestamo[0][2])

                fecha_prestamos_dt = datetime.strptime(datos_prestamo[0][3], FORMATO_BD)
                fecha_prestamo     = fecha_prestamos_dt.strftime(FORMATO_FECHA) 
                ci_usuario         = datos_usuario[0][0]
                nombre_usuario     = datos_usuario[0][1]
                apellido_usuario   = datos_usuario[0][2]
                titulo_libro       = datos_libro[0][1]
                estado_prestamo    = datos_prestamo[0][-1]

                if estado_prestamo == 1:
                    estado_prestamo = 'Activo'
                else:
                    estado_prestamo = 'Devuelto'

                if datos_prestamo[0][4] != None:
                    fecha_devuelto_dt  = datetime.strptime(datos_prestamo[0][4],FORMATO_BD)
                    fecha_devuelto     = fecha_devuelto_dt.strftime(FORMATO_FECHA)
                else:
                    fecha_devuelto = 'N/A'

                if datos_prestamo[0][5] != None:
                    condicion_devuelto = datos_prestamo[0][5]
                else:
                    condicion_devuelto = 'N/A'

                clear()
                print(COLOR_TITULO + 'Préstamo\n')
                print(COLOR_FUENTE + 'ID prestamo        : ',id_consultar)
                print(COLOR_FUENTE + 'Fecha              : ',fecha_prestamo)
                print(COLOR_FUENTE + 'CI                 : ',ci_usuario)
                print(COLOR_FUENTE + f'Nombre             :  {nombre_usuario} {apellido_usuario}')
                print(COLOR_FUENTE + 'Libro              : ',titulo_libro)
                print(COLOR_FUENTE + 'Fecha Devolución   : ',fecha_devuelto)
                print(COLOR_FUENTE + 'Condición Devuelto : ',condicion_devuelto)
                print(COLOR_FUENTE + 'Estado Préstamo    : ',estado_prestamo)

                input(COLOR_INPUT + '\nPulse Enter para continuar\n')
                break
            else:
                input(COLOR_ERROR + 'Préstamo no encontrado.\n')
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')

def listado_prestamos():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Listados Prestamos\n')
            print(COLOR_FUENTE + '1. Activos')
            print(COLOR_FUENTE + '2. Devueltos')
            print(COLOR_FUENTE + '0. Salir')
            opcion = int(input(COLOR_INPUT + 'Ingrese opción: '))
            if opcion in range(0,3):
                if opcion   == 0: break
                elif opcion == 1: listado_prestamos_activos()
                elif opcion == 2: listado_prestamos_devueltos()
            else:
                print(COLOR_ERROR + 'Opción fuera de rango.\n')
        except ValueError:
            input(COLOR_ERROR + 'Opción invalida.\n')

def listado_prestamos_activos():
    clear()
    print(COLOR_TITULO + 'Listado de Prestamos Activos\n')
    sql = 'SELECT id_prestamo, fecha_prestamo, ci_usuario, id_libro FROM prestamos WHERE estado_prestamo = ?'
    parametros = (1,)
    datos_prestamos = correr_consulta(sql,parametros)
    if datos_prestamos != None:
        resultado = []
        for datos_prestamo in datos_prestamos:
            _,datos_usuario  = existe_clave('usuarios','ci_usuario',datos_prestamo[2])
            _,datos_libro    = existe_clave('libros','id_libro',datos_prestamo[3])

            id_prestamo      = datos_prestamo[0]
            fecha_datetime   = datetime.strptime(datos_prestamo[1], FORMATO_BD)
            fecha_formato    = fecha_datetime.strftime(FORMATO_FECHA)
            ci_usuario       = datos_prestamo[2]
            nombre_usuario   = f'{datos_usuario[0][1]} {datos_usuario[0][2]}'
            libro            = datos_libro[0][1]
            resultado.append([id_prestamo,fecha_formato,ci_usuario,nombre_usuario,libro])

        print(COLOR_LISTADO + tabulate(resultado, headers=cabezal_prestamo_activo, tablefmt='orgbiil1', numalign='center'))         
        input(COLOR_INPUT + '\nIngrese Enter para continuar\n')
    else:
        input(COLOR_ERROR + 'No hay prestamos para mostrar.\n')


def listado_prestamos_devueltos():
    clear()
    print(COLOR_TITULO + 'Listado de Prestamos Devueltos\n')
    sql = 'SELECT id_prestamo, fecha_prestamo, ci_usuario, id_libro, fecha_devolucion, condicion_devuelto FROM prestamos WHERE estado_prestamo = ?'
    parametros = (0,)
    datos_prestamos   = correr_consulta(sql,parametros)
    if datos_prestamos != None:
        resultado = []
        for datos_prestamo in datos_prestamos:
            _,datos_usuario     = existe_clave('usuarios','ci_usuario',datos_prestamo[2])
            _,datos_libro       = existe_clave('libros','id_libro',datos_prestamo[3])

            id_prestamo         = datos_prestamo[0]
            fecha_datetime      = datetime.strptime(datos_prestamo[1], FORMATO_BD)
            fecha_formato       = fecha_datetime.strftime(FORMATO_FECHA)
            ci_usuario          = datos_prestamo[2]
            nombre_usuario      = f'{datos_usuario[0][1]} {datos_usuario[0][2]}'
            libro               = datos_libro[0][1]
            fecha_devolucion_dt = datetime.strptime(datos_prestamo[4],FORMATO_BD)
            fecha_devolucion    = fecha_devolucion_dt.strftime(FORMATO_FECHA)
            condicion_devuelto  = datos_prestamo[-1]
            if condicion_devuelto == None:
                condicion_devuelto = 'N\A'

            resultado.append([id_prestamo,fecha_formato,ci_usuario,nombre_usuario,libro,fecha_devolucion,condicion_devuelto])

        print(COLOR_LISTADO + tabulate(resultado, headers=cabezal_prestamo_devuelto, tablefmt='orgbiil1', numalign='center'))         
        input(COLOR_INPUT + '\nIngrese Enter para continuar\n')
    else:
        input(COLOR_ERROR + 'No hay prestamos para mostrar.\n')


def menu_prestamos():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Menu de Prestamos\n')
            print(COLOR_FUENTE + '1. Ingresar Préstamo')
            print(COLOR_FUENTE + '2. Devoluciones')
            print(COLOR_FUENTE + '3. Consulta de Prestamos')
            print(COLOR_FUENTE + '4. Listados varios')
            print(COLOR_FUENTE + '0. Volver al Menu Principal\n') 
            opcion = int(input(COLOR_INPUT + 'Ingrese opcion: '))
            if opcion in range(0,5): 
                if opcion   == 0: break
                elif opcion == 1: ingresar_presatamos()
                elif opcion == 2: devoliciones()
                elif opcion == 3: consultar_prestamo()
                elif opcion == 4: listado_prestamos()
            else:
                input(COLOR_ERROR + 'Opción fuera de rango.\n')
        except ValueError:
            input(COLOR_INPUT + 'Opción invalida.\n')
