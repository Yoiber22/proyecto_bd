from config import *

clear = lambda: os.system('cls')
obligatorio = lambda: input(COLOR_ERROR + 'Campo obligatorio.\n')

def correr_consulta(consulta, parametros=()):
    try:
        conexion = sqlite3.connect(DB_NAME)     # Conectarnos con la Base de Datos
        cursor = conexion.cursor()              # Establecer un cursor
        consulta = cursor.execute(consulta, parametros)
        conexion.commit()
        resultado = consulta.fetchall()
        conexion.close()

        if len(resultado) > 0:
            return resultado
        else:
            return None
        
    except sqlite3.OperationalError as error:
        print('Ocurrió un error en la sql',error)


def ultima_clave(tabla,campo):
    sql = f'select max({campo}) from {tabla}'
    resultado = correr_consulta(sql)
    if resultado[0][0] != None:
        return resultado[0][0]    
    else:
        return 0


def datos_columna(tabla,campo):
    sql = f'SELECT {campo} FROM {tabla}'
    l_tuplas = correr_consulta(sql)
    datos = []
    for tupla in l_tuplas:
        for dato in tupla:
            datos.append(dato)
    return datos


def existe_clave(tabla,campo,valor):
    sql = f'SELECT * FROM {tabla} WHERE {campo} = ?'
    parametros = (valor,)
    resultado = correr_consulta(sql, parametros)
    if resultado != None:
        return True, resultado
    else:
        return False, None 


def validar_seccion(seccion):
    if '-' in seccion and seccion.count('-') == 1:
        l_seccion = seccion.split('-')
        if l_seccion[0].isalpha() and len(l_seccion[0]) == 1: 
            if l_seccion[1].isdigit():
                return True
    return False

def validar_cedula_uruguaya(ci):
    # Verifica una cedula uruguaya con el digito verificador
    ci = ci.replace('-','').replace('.','') 
    if len(ci) == 8 and ci.isdigit(): 
        vector  = [8,1,2,3,4,7,6]       
        ci_digitos = [int(digito) for digito in ci[:7]]     
        digito_verificador = sum(ci_digitos[pos] * vector[pos] for pos in range(7)) % 10                                                                                              
        if digito_verificador == int(ci[-1]):    
            return True, ci                       
    return False, None


def validar_direccion(direccion):
    if len(direccion) > 0:
        geolocator = Nominatim(user_agent='my app')
        try:
            location = geolocator.geocode(direccion + ' ,Uruguay', exactly_one=True)
            if location is not None and 'Uruguay' in location.address:
                return True, location.address
            else:
                return False, None
        except GeocoderTimedOut:
            print('Tiempo de espera agotado. Intente nuevamente más tarde.')
            return False, None
        except GeocoderServiceError as e:
            print(f'Error del servicio de geocodificación: {e}')
            return False, None


def validar_email(email):
    
    if email.count('@') == 1:
        usuario, dominio = email.split('@')
        if len(usuario) > 0 and usuario.isalnum() and not usuario[0].isdigit() and len(dominio) > 0:
            for usuario in dominios:
                    return True
    return False     


def validar_telefono(numero):
    numero = numero.replace(' ','').replace('-','')
    prefijos_celuares = ('093','094','095',       # Movistar
                         '091','092','098','099', # Antel
                         '096','097'              # Claro
                            )
    prefijos_fijos = ('2',   # Montevideo
                      '463', # Tacuarembo
                      '436', # Durazno
                      '444', # Lavalleja
                      '435', # Florida
                      '4364','4385', # Flores
                      '434', # San Jose
                      '452', # Colonia
                      '453', # Soriano
                      '4567','4560','456',# Rio Negro
                      '472', # Paisandu
                      '473', # Salto
                      '477', # Aritgas
                      '462', # Rivera
                      '464', # Cerro Largo
                      '445', # Treinta y Tres
                      '447', # Rocha
                      '442', # Maldonado
                      '433'  # Canelores
                    )
    if len(numero) == 9:
        for prefijo in prefijos_celuares:
            if numero.startswith(prefijo):
                return True, numero

    elif len(numero) == 8:
        for prefijo in prefijos_fijos:
            if numero.startswith(prefijo):
                return True, numero
    return False, None   
