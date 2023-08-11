--INSERT INTO
	--ciudades
	--(nombre_ciudad)
--VALUES
	--('Montevideo'),
	--('Canelones'),
	--('San Jose'),
	--('Maldonado')
	
--SELECT * FROM alumnos

SELECT
	alumnos.id_alumno,
	alumnos.nombre_alumno,
	alumnos.apellido_alumno,
	cursos.nombre_curso,
	ciudades.nombre_ciudad
FROM
	alumnos, cursos, ciudades
WHERE
	alumnos.id_curso = cursos.id_curso AND
	alumnos.id_ciudad = ciudades.id_ciudad
ORDER by
	cursos.nombre_curso ASC
	