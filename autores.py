from funciones import * 

def alta_autores():
    while True:
        id_autor = ultima_clave('autores','id_autor') + 1
        clear()
        print(COLOR_TITULO + 'Alta de Autor\n')
        print(COLOR_FUENTE + 'ID Autor: ',id_autor)
        while True:
            nombre_autor = input('Nombre: ').title()
            if len(nombre_autor) > 0:
                break
            else:
                input(COLOR_ERROR + 'Campo obligatorio.')

        if input(COLOR_INPUT + '\n¿Confirma agregar a este autor? (s/n): ').lower() == 's':
            sql = 'insert into autores (id_autor, nombre_autor, estado_autor) values (?,?,?)'
            parametros = (id_autor,nombre_autor,1)
            correr_consulta(sql,parametros)
            print(COLOR_DESTACAR + 'Autor agregado exitosamente.')

        if input(COLOR_INPUT + '\n¿Desea ingresar a otro autor? (s/n): ').lower() != 's':
            break


def baja_autores():
    # No es posible bajar a un autor que tenga libros asociados
    # Las bajas son un cambio de estado a 0 en el campo estado_autor (no es un DELETE)
    while True:
        try:
        # La baja de autor se hora solicitando el código de autor
            clear()
            print(COLOR_TITULO + 'Baja de Autores\n')
            id_baja = int(input(COLOR_INPUT + 'ID de Autor: '))
            existe_autor, datos_autor = existe_clave('autores','id_autor',id_baja)
            if existe_autor:
                nombre_autor = datos_autor[0][1] 
                if datos_autor[0][2] == 1:
                    print(COLOR_FUENTE + 'Nombre autor: ',nombre_autor)

                    existe, libros = existe_clave('libros','id_autor',id_baja)
                    if not existe: # Si no existe un libro de esta id_baja
                        if input(COLOR_INPUT + '¿Seguro desea dar de baja a este autor ? (s/n): ').lower() == 's':
                            sql = 'UPDATE autores SET estado_autor = ? WHERE id_autor = ?'
                            parametros = (0,id_baja)
                            correr_consulta(sql,parametros)
                            print(COLOR_DESTACAR + 'Autor dado de baja exitosamente\n')
                    else:
                        # Hay libros de ese autor
                        print(COLOR_ERROR + 'Hay libros de ese autor. Imposible borrar.\n')
                        print(COLOR_LISTADO + tabulate(libros, headers= cabezal_libro, tablefmt='orgbiil1', numalign='center'))
                        input(COLOR_INPUT + '\nPuse Enter para continuar\n')
                else:
                    print(COLOR_ERROR + f'El autor {nombre_autor} ya esta dado de baja.\n')
                if input(COLOR_INPUT + '¿Desea dar de baja a otro autor? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'ID no encontrado.\n')            
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')


def reactivar_autor():
    # Reactivar autor dado de baja (Por borrado lógico)
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Reactivar Autor\n')
            id_reactivar = int(input(COLOR_INPUT + 'ID de autor: '))
            existe_autor, datos_autor = existe_clave('autores','id_autor',id_reactivar)
            if existe_autor: # Si existe el autor
                nombre_autor = datos_autor[0][1] 
                if datos_autor[0][2] == 0: # Si esta dado de baja
                    print(COLOR_FUENTE + 'Nombre autor: ',nombre_autor)

                    if input(COLOR_INPUT + '\n¿Seguro desea reactivar a este autor? (s/n): ').lower() == 's':
                        sql = 'UPDATE autores SET estado_autor = ? WHERE id_autor = ?'
                        parametros = (1,id_reactivar)
                        correr_consulta(sql,parametros)
                        print(COLOR_DESTACAR + 'Autor reactivado exitosamente\n')
                else:
                    print(COLOR_ERROR + f'El autor {nombre_autor} no esta dado de baja.\n')
                if input(COLOR_INPUT + '¿Desea reactivar a otro autor? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'Autor no encontrado.\n')
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')


def modificar_autor():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Modificar Autor\n')
            id_modificar = int(input(COLOR_INPUT + 'Id de autor: '))
            existe_autor, datos_autor = existe_clave('autores','id_autor',id_modificar)
            if existe_autor:
                nombre_autor = datos_autor[0][1]
                print(COLOR_FUENTE + 'Nombre autor: ',nombre_autor)

                if input(COLOR_INPUT + '¿Seguro desea modificar a este autor? (s/n): ').lower() == 's':
                    
                    while True:
                        print(COLOR_TITULO + '\nModificar Nombre')
                        nuevo_nombre = input(COLOR_INPUT + 'Nuevo nombre: ').title()
                        if len(nuevo_nombre) > 0:
                            sql = 'UPDATE autores SET nombre_autor = ? WHERE id_autor = ?'
                            parametros = (nuevo_nombre,id_modificar)
                            correr_consulta(sql,parametros)
                            print(COLOR_DESTACAR + 'Autor modificado exitosamente\n')
                            break
                        else:
                            obligatorio()

                if input(COLOR_INPUT + '¿Desea modificar a otro autor? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'Autor no encontrado.\n')
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')


def listado_autores():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Listado de Autores\n')
            print(COLOR_FUENTE + '1. Activos')
            print(COLOR_FUENTE + '2. Dados de baja')
            print(COLOR_FUENTE + '0. Salir')
            opcion = int(input(COLOR_INPUT + 'Ingrese opción: '))
            if opcion in range(0,3):
                if opcion ==0:
                    break

                elif opcion == 1:
                    while True:
                        clear()
                        print(COLOR_TITULO + 'Listado de Autores Activos\n')
                        sql = 'SELECT * FROM autores WHERE estado_autor = ?'
                        parametros = (1,)
                        resultado = correr_consulta(sql, parametros)
                        print(COLOR_LISTADO + tabulate(resultado, headers=cabezal_autor, tablefmt='orgbiil1', numalign='center'))
                        input(COLOR_INPUT + '\nIngrese Enter para continuar\n')
                        break

                elif opcion == 2:
                    while True:
                        clear()
                        print(COLOR_TITULO + 'Listado de Autores Dados de Baja\n')
                        sql = 'SELECT * FROM autores WHERE estado_autor = ?'
                        parametros = (0,)
                        resultado = correr_consulta(sql, parametros)
                        print(COLOR_LISTADO + tabulate(resultado, headers=cabezal_autor, tablefmt='orgbiil1', numalign='center'))
                        input(COLOR_INPUT + '\nIngrese Enter para continuar\n')
                        break
             
            else:
                input(COLOR_ERROR + 'Opción fura de rango.\n')

        except ValueError:
            input(COLOR_ERROR + 'Opción inválida.\n')


def menu_autores():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Menu de Autores\n')
            print(COLOR_FUENTE + '1. Alta de Autores')
            print(COLOR_FUENTE + '2. Baja de Autores')
            print(COLOR_FUENTE + '3. Reactivar Autor')
            print(COLOR_FUENTE + '4. Modificación de Autores')
            print(COLOR_FUENTE + '5. Listado de Autores')
            print(COLOR_FUENTE + '0. Volver al Menu Principal\n') 
            opcion = int(input(COLOR_INPUT + 'Ingrese opcion: ')) 
            if opcion in range(0,6):
                if opcion == 0: break
                elif opcion == 1: alta_autores()
                elif opcion == 2: baja_autores()
                elif opcion == 3: reactivar_autor()
                elif opcion == 4: modificar_autor()
                elif opcion == 5: listado_autores()
            else:
                input(COLOR_ERROR + 'Opción fuera de rango.\n')
        except ValueError:
            input(COLOR_ERROR + 'Opción invalida.\n')