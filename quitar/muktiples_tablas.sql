-- SELECT * FROM alumnos

-- Consultas sobre multiples tablas
-- Si estamos haciendo un SELECT sobre mas de una tabla, tenemos que anteponer
-- el nombre de la tabla al campo (nombre_tabla.nombre_campo)

SELECT
	alumnos.id_alumno,
	alumnos.nombre_alumno,
	alumnos.apellido_alumno,
	cursos.nombre_curso,
	alumnos.fecha_nac
FROM
	alumnos, cursos
WHERE
	alumnos.id_curso = cursos.id_curso