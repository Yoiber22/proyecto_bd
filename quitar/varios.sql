-- Agregar una nueva ciudad - Artigas

INSERT INTO
	ciudades (nombre_ciudad) 
VALUES 
	('Artigaz')

-- Actualizar
-- UPDATE nombre_lista SET nombre_campo = nuevo_valor, .... campo_n = nuevo_valor WHERE lista de condiciones
-- Si la clausula sql no tiene un WHERE actualizara TODOS los campos

UPDATE ciudades SET nombre_ciudad = 'Artigas' WHERE id_ciudad = 5
		
-- Actualizar los compos del alumno nr 10, el nombre es Martina, el apellido es Benites y
-- la ciudad es la numero 3

UPDATE
	alumnos 
SET 
	nombre_alumno = upper('Martina'), 
	apellido_alumno = upper('Benites'),
	id_ciudad = 3
WHERE
	id_alumno = 10
	
-- ROLLBACK deshace un cambio

UPDATE
	alumnos
SET
	edad = 0
	
-- Borrar Registros
-- DELETE FROM nombre_tabla WHERE lista_condiciones
-- Sin un WHERE borra todos los campos

UPDATE cursos SET estado = 1

DELETE FROM cursos WHERE id_curso = 13

INSERT INTO cursos (nombre_curso,estado) VALUES ('Cocina',1)

-- Formato de Fecha en las bases de datos iso_8609	aaaa-mm-dd
-- Formato hora 24hs  HH:MM

