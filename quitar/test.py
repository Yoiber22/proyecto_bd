from funciones import *

# Ver todos los alumnos de la tabla 'alumnos'
# Para ejecutar una instruccion sql se usa el metodo cursor.execute()
# El metodo execute tiene 2 parametros
# cursor.execute(string, tupla)
# El string es la instruccion sql
# La tupla son paraetros quepueden ser usados en ese string

# sql = 'select * from alumnos'
# consulta = cursor.execute(sql)

# resultado = consulta.fetchall() # Devuelve una lista de tuplas

# print(tabulate(resultado, headers=cabezal, tablefmt='rounded_outline', numalign='center'))

# # Deseo ver los datos del alumno nro 1
# sql = 'select * from alumnos where id_alumno = ?'
# parametros = (1,)
# resultado = correr_consulta(sql, parametros)
# print(tabulate(resultado, headers=cabezal, tablefmt='rounded_outline', numalign='center'))


# print(tabulate([resultado], headers=cabezal, tablefmt='rounded_outline', numalign='center'))

# Deseamos ver todos los alumnos que cursan Python y son de Montevideo

# sql = 'select * from alumnos where id_curso = ? and id_ciudad = ?'
# parametros = (12,1)
# resultado = correr_consulta(sql,parametros)
# if resultado != None:
#     print(tabulate(resultado, headers=cabezal, tablefmt='rounded_outline', numalign='center'))
# else:
#     print('Nada que mostrar')

# Deseamos ingresar un nuevo curso

nombre = 'Lenguaje C'
sql = 'insert into cursos (nombre_curso, estado) values (?,?)'
parametros = (nombre,1)
# correr_consulta(sql,parametros)
# print('\nCurso agregado exitosamente\n')

sql = 'update cursos set estado = ? where id_curso = ?'
parametros = (0,15)
# correr_consulta(sql,parametros)
# print('Cursos dado de baja existosamente (baja logica)')

# Mostrar en pantalla toda la informacion de los alumnos que sean de Montevideo


sql = '''SELECT
            alumnos.id_alumno,
            alumnos.apellido_alumno,
            alumnos.nombre_alumno,
            cursos.nombre_curso,
            alumnos.fecha_nac,
            ciudades.nombre_ciudad
        FROM
	        alumnos,ciudades,cursos
        WHERE
            alumnos.id_ciudad = ciudades.id_ciudad AND
            alumnos.id_curso = cursos.id_curso AND
            alumnos.id_ciudad = ? '''

parametros = (1,)
resultado = correr_consulta(sql,parametros)

if resultado != None:
    clear()
    cabezal = ['Nro','Apellido','Nombre','Curso','Fecha Nac','Ciudad']
    print(tabulate(resultado, headers=cabezal, tablefmt='rounded_outline', numalign='center'))
    print()
else:
    print('No hay datos para mostrar')


