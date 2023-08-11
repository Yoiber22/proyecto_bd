-- insertados: En base de datos, hablar de una insercion significa "agregar" registros
-- Sintaxis: INSERT INTO nombre_tabla (lista_campos) VALUES (lista_de_valore)

INSERT INTO
	cursos 
		(nombre_curso) 
	VALUES 
		('WINDOWS BASICO'),('FORTRAN'),('JAVA')
		
-- Agregar 5 alumnos mas a la tabla Alumnos (con la clave foranea)

INSERT INTO
	alumnos
	(nombre_alumno,apellido_alumno,id_curso,fecha_nac,edad)
VALUES
	('MARTIN','BENITEZ',2,'22/08/1981',0),
	('ALEJANDRA','CORREA',1,'1/10/2003',0),
	('PAOLA','CORDOBA',1,'26/03/2005',0),
	('GUILLERMO','DEVIDA',5,'29/01/1972',0)
	
- COMMIT()
		
-- En sqlite los acmpos booleanos "no existen" como tal, sin embargo se pueden
-- considerar como True el 1 y False el 0		