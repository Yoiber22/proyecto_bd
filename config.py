import pathlib
from tabulate import tabulate
from colorama import Fore, Back, Style, init
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import sqlite3
import os
import sys


PATH = pathlib.Path(__file__).parent.absolute() # obtenemos el path absoluto de este archivo
PATH = str(PATH) # lo convertimos a string
PATH = PATH.replace('\\', '/') # reemplazamos las diagonales invertidas por diagonales normales

# Base de datos
PATH_DATA = PATH + '/data'

DB_NAME = PATH_DATA +'/biblioteca.db'

# Carpeta de imágenes
PATH_DATA = PATH + '/images'

# Colores básicos
COLOR_TITULO      = Fore.CYAN
COLOR_FUENTE      = Fore.LIGHTWHITE_EX
COLOR_INPUT       = Fore.LIGHTBLUE_EX
COLOR_ERROR       = Fore.RED
COLOR_DESTACAR    = Fore.LIGHTGREEN_EX
COLOR_LISTADO     = Fore.LIGHTWHITE_EX

# Títulos de los listados
cabezal_autor             = ['ID','Nombre','Estado']
cabezal_categoria         = ['ID','Descripción','Sección']
cabezal_libro             = ['ID','Titulo','Autor','Categoría','Año Edición','Copias','Estado']
cabezal_usuario           = ['Cédula','Nombre','Apellido','Dirección','Departamento','Teléfono','Email','Edad','Estado']
cabezal_prestamo_activo   = ['ID Préstamo','Fecha Entregado','CI Usuario','Nombre Usuario','Libro']
cabezal_prestamo_devuelto = ['ID Préstamo','Fecha Entregado','CI Usuario','Nombre Usuario','Libro','Fecha Devuelto','Condición Devuelto']

# Fecha Actual
anio_acual = datetime.now().year
fecha_actual = datetime.now()

# Formatos de Fecha y Hora
FORMATO_FECHA   = '%d/%m/%Y'
FORMATO_HORA    = '&H:%M'
FORMATO_HORA_12 = '%I:%M %p'    # Formato 12 hs  
FORMATO_BD      = '%Y-%m-%d'

# Datos geograficos
DEPARTAMENTOS = ('''Artigas, Canelones, Cerro Largo, Colonia,
                  Durazno, Flores, Florida, Lavalleja, Maldonado,
                  Montevideo, Paysandu, Rio Negro, Rivera, Rocha,
                  Salto, San Jose, Soriano, Tacuarembo, Treinta y Tres
                 ''')

# Dominios Validos
dominios =  ("gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"
                 ".uy", ".com.uy", ".edu.uy", ".net.uy", ".gub.uy")