--SQL -LENGUAJE DE CONSULTA ESTRUCTURADO

-- Intruccion Select --> Consultas
-- sintaxis  = select lista_de_campos from lista_tablas where lista_condiciones oreder by lista_campos group by lista_campos
-- Cuando consultamos una sola tabla podemos usar en la lista de capos el comodin * --> todos los campos

select * from cursos
select * from alumnos

select nombre_curso as curso,id_curso as id from cursos

select * from alumnos order by apellido_alumno, nombre_alumno DESC

SELECT id_alumno, nombre_alumno, apellido_alumno FROM alumnos ORDER by id_alumno DESC

-- Supongamos que deseamos ver los alumnos cuyos id_alumno esten entre el 2 y el 5
SELECT * FROM alumnos WHERE id_alumno >=2 AND id_alumno <=5 ORDER by apellido_alumno,nombre_alumno

-- Queremos averiguar todos los "Perez" que hay en la tabla de alumnos
SELECT * FROM alumnos WHERE apellido_alumno = "PEREZ"

-- Realizar una consulta que muestre todos los alumnos de Python
SELECT * FROM alumnos WHERE id_alumno = 1 AND nombre_alumno = 'JUAN'
