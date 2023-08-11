SELECT count(*) as cant FROM alumnos

-- Deseo saber cuantos alumnos hay en cada departamento

SELECT
	ciudades.nombre_ciudad as ciudad,
	count(*) as cant
FROM
	alumnos, ciudades
WHERE
	alumnos.id_ciudad = ciudades.id_ciudad
GROUP by 
	alumnos.id_ciudad

