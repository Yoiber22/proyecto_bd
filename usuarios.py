from funciones import * 

def alta_usuarios():
    while True:
        clear()
        print(COLOR_TITULO + 'Ingresar Usuario\n')

        while True:
            ci_usuario = input(COLOR_INPUT + 'Ingrese cédula: ')
            resultado,ci_usuario = validar_cedula_uruguaya(ci_usuario)
            if resultado:
                ci_registradas = datos_columna('usuarios','ci_usuario',)
                if ci_usuario not in ci_registradas:
                    print(COLOR_FUENTE + 'CI usuario: ',ci_usuario)
                    break
                else:
                    print(COLOR_ERROR + 'Cédula ya agregada.\n')
                if input(COLOR_INPUT + '\n¿Desea continuar? (s/n): ').lower() == 's':
                    return
            else:
                print(COLOR_ERROR + 'Cédula inválida.\n')

        while True:
            nombre_usuario = input(COLOR_INPUT + 'Nombre: ').title()
            if len(nombre_usuario) > 0:
                break
            else:
                obligatorio()
        
        while True:
            apellido_usuario = input(COLOR_INPUT + 'Apellido: ').title()
            if len(apellido_usuario) > 0:
                break
            else:
                obligatorio()

        while True:
            departamento = input(COLOR_INPUT + 'Departamento: ').title()
            if departamento in DEPARTAMENTOS:
                    break
            else:
                print(COLOR_ERROR + 'Departamento inválido.')

        while True:
            direccion_usuario = input(COLOR_INPUT + 'Dirección: ').title()
            if len(direccion_usuario) > 3 and validar_direccion(direccion_usuario + f', {departamento}'):
                    break
            else:
                print(COLOR_ERROR + 'Dirección inválida.')

        while True:
            if input(COLOR_INPUT + '\n¿Desea agregar teléfono? (s/n): ').lower() == 's':
                telefono = (input(COLOR_INPUT + 'Teléfono (opcional): '))
                resultado, telefono = validar_telefono(telefono)
                if resultado:
                    break
                else:
                    print(COLOR_ERROR + 'Teléfono Inválido.\n')
            else:
                telefono = None
                break

        while True:
            if input(COLOR_INPUT + '\n¿Desea ingresar email? (s/n): ').lower() == 's':
                email = input(COLOR_INPUT + 'Email (opcional): ').lower()
                if len(email) > 0:
                    if validar_email(email):
                        break
                    else:
                        print(COLOR_ERROR + 'Email inválido.\n')
                else:
                    obligatorio()
            else:
                email = None
                break

        while True:
            try:
                edad = int(input(COLOR_INPUT + 'Edad: '))
                if edad in range(1,111):
                    break
                else:
                    print(COLOR_ERROR + 'Edad fuera de rango.\n')
            except ValueError:
                input(COLOR_ERROR + 'Edad inválida.')

        clear()
        print(COLOR_TITULO + 'Usuario a ingresar')
        print(COLOR_FUENTE + 'CI          : ',ci_usuario)
        print(COLOR_FUENTE + 'Nombre      : ',nombre_usuario)
        print(COLOR_FUENTE + 'Apellido    : ',apellido_usuario)
        print(COLOR_FUENTE + 'Dirección   : ',direccion_usuario)
        print(COLOR_FUENTE + 'Departamento: ',departamento)
        print(COLOR_FUENTE + 'Teléfono    : ',telefono)
        print(COLOR_FUENTE + 'Email       : ',email)
        print(COLOR_FUENTE + 'Edad        : ',edad)

        if input(COLOR_INPUT + '\n¿Seguro desea agregar a este usuario? (s/n): ').lower() == 's':
            sql = '''INSERT INTO
                        usuarios (ci_usuario,nombre_usuario,apellido_usuario,direccion,departamento,telefono,email,edad,estado_usuario)
                    VALUES
                        (?,?,?,?,?,?,?,?,?)'''
            parametros = (ci_usuario,nombre_usuario,apellido_usuario,direccion_usuario,departamento,telefono,email,edad,1)
            correr_consulta(sql,parametros)
            print(COLOR_DESTACAR + 'Usuario agregado exitosamente\n')

        if input(COLOR_INPUT + '¿Desea agregar otro usuario? (s/n): ').lower() != 's':
            break


def baja_usuarios():
    while True:
        clear()
        print(COLOR_TITULO + 'Baja de Usuarios\n')
        ci_baja = input(COLOR_INPUT + 'CI de usuario: ')
        existe_usuario, datos_usuario= existe_clave('usuarios','ci_usuario',ci_baja)
        if existe_usuario:
            nombre_usuario = datos_usuario[0][1] 
            if datos_usuario[0][-1] == 1:
                print(COLOR_FUENTE + 'Nombre: ',nombre_usuario)

                if input(COLOR_INPUT + '\n¿Seguro desea dar de baja a este usuario? (s/n): ').lower() == 's':
                    sql = 'UPDATE usuarios SET estado_usuario = ? WHERE ci_usuario = ?'
                    parametros = (0,ci_baja)
                    correr_consulta(sql,parametros)
                    print(COLOR_DESTACAR + 'Usuario dado de baja exitosamente\n')
            else:
                print(COLOR_ERROR + f'El Usuario {nombre_usuario} ya esta dado de baja.\n')
            if input(COLOR_INPUT + '¿Desea dar de baja a otro usuario? (s/n): ').lower() != 's':
                break
        else:
            input(COLOR_ERROR + 'CI no encontrada.\n')
            


def reactivar_usuario():
    # Reactivar libro dado de baja (Por borrado lógico)
    while True:
        clear()
        print(COLOR_TITULO + 'Reactivar Usuario\n')
        ci_reactivar = input(COLOR_INPUT + 'CI de usuario: ')
        existe_usuario, datos_usuario = existe_clave('usuarios','ci_usuario',ci_reactivar)
        if existe_usuario: # Si existe el usuario
            nombre_usuario = datos_usuario[0][1] 
            if datos_usuario[0][-1] == 0: # Si esta dado de baja
                print(COLOR_FUENTE + 'Usuario: ',nombre_usuario)

                if input(COLOR_INPUT + '\n¿Seguro desea reactivar a este usuario? (s/n): ').lower() == 's':
                    sql = 'UPDATE usuarios SET estado_usuario = ? WHERE ci_usuario = ?'
                    parametros = (1,ci_reactivar)
                    correr_consulta(sql,parametros)
                    print(COLOR_DESTACAR + 'Usuario reactivado exitosamente\n')
            else:
                print(COLOR_ERROR + f'El usuario {nombre_usuario} no esta dado de baja.\n')

            if input(COLOR_INPUT + '¿Desea reactivar otro usuario? (s/n): ').lower() != 's':
                break
        else:
            input(COLOR_ERROR + 'Usuario no encontrado.\n')


def modificar_usuarios():
    while True:
        clear()
        print(COLOR_TITULO + 'Modificar Usuario\n')
        ci_modificar = input(COLOR_INPUT + 'CI usuario: ')
        existe_usuario, datos_usuario = existe_clave('usuarios','ci_usuario',ci_modificar)

        if existe_usuario:
            if datos_usuario[0][4] == None:
                telefono = 'N/A'
            else:
                telefono = datos_usuario[0][4]
            if datos_usuario[0][5] == None:
                email = 'N/A'
            else:
                email = datos_usuario[0][5]
            clear()
            print(COLOR_TITULO + 'Datos del Usuario\n')
            print(COLOR_FUENTE + 'CI          : ',datos_usuario[0][0])
            print(COLOR_FUENTE + 'Nombre      : ',datos_usuario[0][1])
            print(COLOR_FUENTE + 'Apellido    : ',datos_usuario[0][2])
            print(COLOR_FUENTE + 'Departamento: ',datos_usuario[0][3])
            print(COLOR_FUENTE + 'Dirección   : ',datos_usuario[0][4])
            print(COLOR_FUENTE + 'Teléfono    : ',telefono)
            print(COLOR_FUENTE + 'Email       : ',email)
            print(COLOR_FUENTE + 'Edad        : ',datos_usuario[0][6])

            if input(COLOR_INPUT + '\n¿Seguro desea modificar a este usuario? (s/n): ').lower() == 's':

                while True:
                    print(COLOR_TITULO + 'Campo a modificar\n')
                    print(COLOR_FUENTE + '1. Nombre')
                    print(COLOR_FUENTE + '2. Apellido')
                    print(COLOR_FUENTE + '3. Dirección')
                    print(COLOR_FUENTE + '4. Teléfono')
                    print(COLOR_FUENTE + '5. Email')
                    print(COLOR_FUENTE + '6. Edad')
                    print(COLOR_FUENTE + '0. Salir\n')
                    opcion = int(input(COLOR_INPUT + 'Ingrese campo a modificar: '))
                    if opcion in range(0,7):

                        if opcion == 0:
                            break
                        
                        elif opcion == 1:        
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar el nombre? (s/n): ').lower() =='s':
                                    nuevo_nombre = input(COLOR_INPUT + 'Nuevo nombre: ').title()
                                    if len(nuevo_nombre) > 0:
                                        sql = 'UPDATE usuarios SET nombre_usuario = ? WHERE ci_usuario = ?'
                                        parametros = (nuevo_nombre,ci_modificar)
                                        correr_consulta(sql,parametros)
                                        print(COLOR_DESTACAR + 'Usuario modificado exitosamente\n')
                                        break
                                    else:
                                        obligatorio()
                                else:
                                    break
                            if input(COLOR_INPUT + '¿Desea modificar otro campo? (s/n): ').lower() != 's':
                                break
                                
                        elif opcion == 2:
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar el apellido? (s/n): ').lower() =='s':
                                    nuevo_apellido = input(COLOR_INPUT + 'Nuevo apellido: ')
                                    if len(nuevo_apellido) > 0:
                                        sql = 'UPDATE usuarios SET apellido_usuario = ? WHERE ci_usuario = ?'
                                        parametros = (nuevo_apellido,ci_modificar)
                                        correr_consulta(sql,parametros)
                                        print(COLOR_DESTACAR + 'Usuario modificado exitosamente\n')
                                        break
                                    else:
                                        obligatorio()
                                else:
                                    break
                            if input(COLOR_INPUT + '¿Desea modificar otro campo? (s/n): ').lower() != 's':
                                break  

                        elif opcion == 3:
                            while True:
                                nuevo_departamento = input(COLOR_INPUT + 'Departamento: ').title()
                                if nuevo_departamento in DEPARTAMENTOS:
                                        break
                                else:
                                    print(COLOR_ERROR + 'Departamento inválido.')

                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar la direccion? (s/n): ').lower() =='s':
                                    nueva_direccion = input(COLOR_INPUT + 'Nueva direccion: ').title()
                                    if len(nueva_direccion) > 3 and validar_direccion(nueva_direccion + f', {nuevo_departamento}'):
            
                                        sql = 'UPDATE usuarios SET departamendo = ? WHERE ci_usuario = ?'
                                        parametros = (nuevo_departamento,ci_modificar)
                                        correr_consulta(sql,parametros)

                                        sql = 'UPDATE usuarios SET direccion = ? WHERE ci_usuario = ?'
                                        parametros = (nueva_direccion,ci_modificar)
                                        correr_consulta(sql,parametros)
                                        print(COLOR_DESTACAR + 'Usuario modificado exitosamente\n')
                                        break         
                                    else:
                                        input(COLOR_ERROR + 'Dirección inválida.')
                                else:
                                    break
                            if input(COLOR_INPUT + '¿Desea modificar otro campo? (s/n): ').lower() != 's':
                                break

                        elif opcion == 4:
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar el telefono? (s/n): ').lower() =='s':
                                    nuevo_telefono = input(COLOR_INPUT + 'Teléfono (opcional): ')
                                    resultado, nuevo_telefono = validar_telefono(nuevo_telefono)
                                    if resultado:
                                        sql = 'UPDATE usuarios SET telefono = ? WHERE ci_usuario = ?'
                                        parametros = (nuevo_telefono,ci_modificar)
                                        correr_consulta(sql,parametros)
                                        print(COLOR_DESTACAR + 'Usuario modificado exitosamente\n')
                                        break
                                    else:
                                        input(COLOR_ERROR + 'Teléfono Inválido.')
                                else:
                                    break
                            if input(COLOR_INPUT + '¿Desea modificar otro campo? (s/n): ').lower() != 's':
                                break

                        elif opcion == 5:
                            while True:
                                if input(COLOR_INPUT + '\n¿Seguro desea modificar el email? (s/n): ').lower() =='s':
                                    nuevo_email = input(COLOR_INPUT + 'Email (opcional): ').lower()
                                    if validar_email(nuevo_email):
                                        sql = 'UPDATE usuarios SET email = ? WHERE ci_usuario = ?'
                                        parametros = (nuevo_email,ci_modificar)
                                        correr_consulta(sql,parametros)
                                        print(COLOR_DESTACAR + 'Usuario modificado exitosamente\n')
                                        break
                                    else:
                                        input(COLOR_ERROR + 'Email inválido.')
                                else:
                                    break
                            if input(COLOR_INPUT + '¿Desea modificar otro campo? (s/n): ').lower() != 's':
                                break

                        elif opcion == 6:
                            while True:
                                try:
                                    if input(COLOR_INPUT + '\n¿Seguro desea modificar la edad? (s/n): ').lower() =='s':    
                                        nueva_edad = int(input(COLOR_INPUT + 'Nueva edad: '))
                                        if nueva_edad in range(1,111):
                                            sql = 'UPDATE usuarios SET edad = ? WHERE ci_usuario = ?'
                                            parametros = (nueva_edad,ci_modificar)
                                            correr_consulta(sql,parametros)
                                            print(COLOR_DESTACAR + 'Usuario modificado exitosamente\n')
                                            break
                                        else:
                                            print(COLOR_ERROR + 'Edad fuera de rango.')
                                    else: 
                                        break
                                except ValueError:
                                    input(COLOR_ERROR + 'Edad inválida.')
                            if input(COLOR_INPUT + '¿Desea modificar otro campo? (s/n): ').lower() != 's':
                                break

                    else:
                        input(COLOR_ERROR + 'Opción fuera de rango.\n')

            if input(COLOR_INPUT + '\n¿Desea modificar a otro usuario? (s/n): ').lower() != 's':
                break 
        else:
            input(COLOR_ERROR + 'Usuario no encontrado.\n')


def listado_usuarios():
    clear()
    print(COLOR_TITULO + 'Listado de Usuarios\n')
    sql = 'SELECT * FROM usuarios'
    datos_usuarios = correr_consulta(sql)
    if datos_usuarios != None:
        resultado = []
        for datos_usuario in datos_usuarios:
            ci_usuario   = datos_usuario[0]
            nombre       = datos_usuario[1]
            apellido     = datos_usuario[2]
            direccion    = datos_usuario[3]
            departamento = datos_usuario[4]
            telefono     = datos_usuario[5]
            email        = datos_usuario[6]
            edad         = datos_usuario[7]
            estado       = datos_usuario[-1]
            if estado == 1:
                estado = 'Activo'
            else:
                estado = 'Baja'
            if telefono == None:
                telefono = 'N/A'    
            if email == None:
                email = 'N/A'
            
            resultado.append([ci_usuario,nombre,apellido,direccion,departamento,telefono,email,edad,estado])

        print(COLOR_LISTADO + tabulate(resultado, headers=cabezal_usuario, tablefmt='orgbiil1', numalign='center'))         
        input(COLOR_INPUT + '\nIngrese Enter para continuar\n')
    else:
        input(COLOR_ERROR + 'No hay usuarios para mostrar.\n')

def menu_usuarios():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Menu de Usuarios\n')
            print(COLOR_FUENTE + '1. Alta de Usuarios')
            print(COLOR_FUENTE + '2. Baja de Usuarios')
            print(COLOR_FUENTE + '3. Reactivar Usuario')
            print(COLOR_FUENTE + '4. Modificación de Usuarios')
            print(COLOR_FUENTE + '5. Listado de Usuarios')
            print(COLOR_FUENTE + '0. Volver al Menu Principal\n') 
            opcion = int(input(COLOR_INPUT + 'Ingrese opcion: ')) 
            if opcion in range(0,6):
                if opcion   == 0: break
                elif opcion == 1: alta_usuarios()
                elif opcion == 2: baja_usuarios()
                elif opcion == 3: reactivar_usuario()
                elif opcion == 4: modificar_usuarios()
                elif opcion == 5: listado_usuarios()
            else:
                input(COLOR_ERROR + 'Opción fuera de rango.\n')
        except ValueError:
            input(COLOR_INPUT + 'Opción invalida.\n')
