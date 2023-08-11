-- select -- me permite ralizar consultas en una base de datos
-- El resultado de un selec genera una vista
-- SELECT lista_de_campos from lista_ tablas WHERE lista_condiciones ORDER by lista_de_campos GROUP by lista_campos

SELECT
	id_alumno as ID,
	nombre_alumno as Nombre,
	apellido_alumno as Apellido,
	fecha_nac as Fecha
FROM 
	alumnos
WHERE
	apellido_alumno != 'PEREZ' AND
	apellido_alumno = 'GOMEZ'
ORDER by
	id_alumno DESC