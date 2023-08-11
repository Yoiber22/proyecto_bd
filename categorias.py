from funciones import * 

def alta_categorias():
    while True:
        id_categoria = ultima_clave('categorias','id_categoria') + 1
        clear()
        
        print (COLOR_TITULO + 'Alta de Categorias\n')
        print (COLOR_FUENTE + 'Nro Categoría: ',id_categoria)
        while True:
            nombre_categoria = input(COLOR_INPUT + 'Descripción: ').upper()
            if len(nombre_categoria) >0:
                break
            else:
                obligatorio()

        while True :  # Para la seccion - Letra-Numero (A-1)
            seccion_cat = input(COLOR_INPUT + 'Sección (A-1): ').upper()
            if validar_seccion(seccion_cat):
                break
            else:
                input(COLOR_ERROR + 'Formato no válido (letra-numero).\n')
        clear()   
        print(COLOR_FUENTE + 'Categoría : ',nombre_categoria)
        print(COLOR_FUENTE + 'Sección   : ',seccion_cat)
        
        if input(COLOR_INPUT + '\n¿Confirma ingresar esta categoría? (s/n): ').lower() == 's':
            sql = '''INSERT INTO
                         categorias (id_categoria, nombre_categoria, seccion_categoria)
                    VALUES 
                        (?,?,?)'''
                    
            parametros = (id_categoria, nombre_categoria,seccion_cat)
            correr_consulta(sql, parametros)
            print (COLOR_DESTACAR + 'Categoría agregada exitosamente\n')
        
        if input(COLOR_INPUT + '\n¿Desea ingresar a otra categoría? (s/n): ').lower() != 's':
            break


def baja_categorias():
    # No es posible bajar a una categoria que tenga libros asociados
    # Las bajas son un borrado físico
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Baja de Categorías\n')
            id_baja = int(input(COLOR_INPUT + 'ID de Categoría: '))
            existe_cat, datos_cat = existe_clave('categorias','id_categoria',id_baja)
            if existe_cat:
                categoria = datos_cat[0][1] 
                print(COLOR_FUENTE + 'Categoría: ',categoria)

                existe, libros = existe_clave('libros','id_categoria',id_baja)
                if not existe: # Si no existe un libro de esta id_baja
                    if input(COLOR_INPUT + '\n¿Seguro desea eliminar esta categoria ? (s/n): ').lower() == 's':
                        sql = 'DELETE FROM categorias WHERE id_categoria = ?'
                        parametros = (id_baja,)
                        correr_consulta(sql,parametros)
                        print(COLOR_DESTACAR + 'Categoría eliminada exitosamente\n')
                else:
                    # Hay libros en esa categoria
                    print(COLOR_ERROR + '\nHay libros en esta categoria. Imposible borrar.')
                    print(COLOR_LISTADO + tabulate(libros, headers= cabezal_libro, tablefmt='rounded_outline', numalign='center'))
                    input(COLOR_INPUT + '\nPuse Enter para continuar\n')
                if input(COLOR_INPUT + '¿Desea eliminar otra categoria? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'ID no encontrado.\n')    
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')


def modificar_categoria():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Modificar Categoría\n')
            id_modificar = int(input(COLOR_INPUT + 'Id categoria: '))
            existe_cat, datos_cat = existe_clave('categorias','id_categoria',id_modificar)
            if existe_cat:
                clear()
                print(COLOR_FUENTE + 'ID categoria      : ',datos_cat[0][0])
                print(COLOR_FUENTE + 'Descripción       : ',datos_cat[0][1])
                print(COLOR_FUENTE + 'Sección categoria : ',datos_cat[0][2])

                if input(COLOR_INPUT + '\n¿Seguro desea modificar esta categoria? (s/n): ').lower() == 's':  

                    while True:
                        try:
                            print(COLOR_TITULO + '\nCampo a Modificar\n')
                            print(COLOR_FUENTE + '1. Descripción')
                            print(COLOR_FUENTE + '2. Sección')
                            print(COLOR_FUENTE + '0. Salir\n')
                            opcion = int(input(COLOR_INPUT + 'Ingrese campo a modificar: '))

                            if opcion == 0:
                                break

                            elif opcion == 1:
                                while True:
                                    if input(COLOR_INPUT + '\n¿Seguro desea modificar la descripción? (s/n): ').lower() =='s':
                                        print(COLOR_TITULO + '\nModificar Descripción\n')
                                        nuevo_nombre = input(COLOR_INPUT + 'Nueva descripción: ').upper()
                                        if len(nuevo_nombre) > 0:
                                            sql = 'UPDATE categorias SET nombre_categoria = ? WHERE id_categoria = ?'
                                            parametros = (nuevo_nombre,id_modificar)
                                            correr_consulta(sql,parametros)
                                            print(COLOR_DESTACAR + 'Categoria modificada exitosamente\n')
                                            break
                                        else:
                                            obligatorio()
                                    else:
                                        modificar_categoria()

                            elif opcion == 2:

                                while True :  # Para la seccion - Letra-Numero (A-1)
                                    if input(COLOR_INPUT + '\n¿Seguro desea modificar la seccion? (s/n): ').lower() =='s':
                                        print(COLOR_TITULO + '\nModificar Sección\n')
                                        nueva_seccion_cat = input('Sección (A-1): ').upper()
                                        if validar_seccion(nueva_seccion_cat):
                                            sql = 'UPDATE categorias SET seccion_categoria = ? WHERE id_categoria = ?'
                                            parametros = (nueva_seccion_cat,id_modificar)
                                            correr_consulta(sql,parametros)
                                            print(COLOR_DESTACAR + 'Categoria modificada exitosamente\n')
                                            break
                                        else:
                                            input(COLOR_ERROR + 'Formato no válido (letra-numero.)\n')
                                    else:
                                        modificar_categoria()
                        except ValueError:
                            input(COLOR_ERROR + 'ID Inválida.\n')

                if input(COLOR_INPUT + '¿Desea modificar otra categoria? (s/n): ').lower() != 's':
                    break
            else:
                input(COLOR_ERROR + 'ID no encontrado.\n')
        except ValueError:
            input(COLOR_ERROR + 'ID inválida.\n')

def listado_categirioas():
    clear()
    print(COLOR_TITULO + 'Listado de Categorías\n')
    sql = 'SELECT * FROM categorias'
    resultado = correr_consulta(sql)
    if existe_clave('categorias','id_categoria',resultado[0][0]):
        print(COLOR_LISTADO + tabulate(resultado, headers=cabezal_categoria, tablefmt='orgbiil1', numalign='center'))         
        input(COLOR_INPUT + '\nIngrese Enter para continuar\n')
    else:
        input(COLOR_ERROR + 'Sin datos para mostrar.\n')
    

def menu_categorias():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Menu de Categorías\n')
            print(COLOR_FUENTE + '1. Alta de Categorías')
            print(COLOR_FUENTE + '2. Baja de Categorías')
            print(COLOR_FUENTE + '3. Modificación de Categorías')
            print(COLOR_FUENTE + '4. Listado de Categorías')
            print(COLOR_FUENTE + '0. Volver al Menu Principal\n') 
            opcion = int(input(COLOR_INPUT + 'Ingrese opcion: ')) 
            if opcion in range(0,5):
                if opcion   == 0: break
                elif opcion == 1: alta_categorias()
                elif opcion == 2: baja_categorias()
                elif opcion == 3: modificar_categoria()   
                elif opcion == 4: listado_categirioas()
            else:
                input(COLOR_ERROR + 'Opción fuera de rango.\n')
        except ValueError:
            input(COLOR_INPUT + 'Opción invalida.\n')
