from funciones import *

# Deseamos saber que alumnos cursan Python (id_curso = 1)
sql = 'SELECT * FROM alumnos WHERE id_curso = ? AND id_ciudad = ?'
parametros = (1,1)
resultado = correr_consulta(sql,parametros)

print(resultado)

# Borrar todos los alumnos de la ciudad nro 4
sql = 'DELETE FROM alumnos WHERE id_alumno = ?'
parametros = (3,)
correr_consulta(sql, parametros)
print('Alumnos de la ciudad 4 eliminados...')

# Pasar todos los alumnos de la ciudad 3 a la 1
sql = 'UPDATE alumnos SET id_ciudad = ? WHERE id_ciudad = ?'
parametros = (1,3)
# correr_consulta(sql, parametros)
# print('Alumnos actualizados correctamente...')