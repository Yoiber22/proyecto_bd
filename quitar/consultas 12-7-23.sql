-- INSERT INTO nombre_tabla (campos_tabla) VALUES (los valores de los campos)

-- INSERT INTO cursos (nombre_curso) VALUES ('ASSEMBLER'),('C#'),('JAVA SCRIPT')

--SELECT 
	--id_curso as ID,
	--nombre_curso as Curso 
--FROM
	--cursos
--WHERE
	--nombre_curso != 'COBOL'
--ORDER BY 
	--nombre_curso ASC
	
SELECT
	* 
FROM
	alumnos
WHERE
	id_curso = 1
ORDER BY
	apellido_alumno, nombre_alumno
	
-- Cuantos registros tiene la tabla alumnos

SELECT count(*) as Cantidad FROM alumnos

-- GROUP by
-- Deseo saber cuantos alumnos hay en cada curso 

SELECT id_curso, count(*) as cant FROM alumnos GROUP by id_curso

SELECT 
	apellido_alumno, 
	nombre_alumno,
	id_curso
FROM
	alumnos
WHERE
	id_curso = 1

-- Ver todos los apellidos
	
SELECT apellido_alumno FROM alumnos GROUP by apellido_alumno

-- DISTINCT

SELECT DISTINCT apellido_alumno FROM alumnos




