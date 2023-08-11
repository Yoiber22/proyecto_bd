from funciones import *

'''
insert into nombre_tabla  (lista_de_campos) values (lista_valores)
# Que en el caso de la PK fuera AI, no era necesario ponerla en la instruccion

'''

clave_alumno = ultima_clave('alumnos','id_alumno') + 1

sql = "insert into alumnos values (?,?,?,?,?,?,?)"
parametros = (clave_alumno,'JAVIER','PAREDES',1,'14/01/1991',0,3)
correr_consulta(sql, parametros)

# clave_ciudad = ultima_clave('ciudades','id_ciudad')
# nombre_ciudad = 'Rivera'
# sql = 'insert into ciudades values (?,?)'
# parametros = (clave_ciudad, nombre_ciudad)
# correr_consulta(sql,parametros)

ci = '62377055'
p = [int(digito) for digito in ci[:7]]
v  = [8,1,2,3,4,7,6]
r = sum(p[i] * v[i] for i in range(7)) % 10
if r == int(ci[-1]):
    print('True')
else:
    print('False')