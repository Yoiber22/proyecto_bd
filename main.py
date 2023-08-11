from funciones import *
import libros, autores, categorias, usuarios, prestamos

init(autoreset = True)

def menu_principal():
    while True:
        try:
            clear()
            print(COLOR_TITULO + 'Menu Principal Biblioteca\n')
            print(COLOR_FUENTE + '1. Libros')
            print(COLOR_FUENTE + '2. Autores')
            print(COLOR_FUENTE + '3. Categorías')
            print(COLOR_FUENTE + '4. Usuarios')
            print(COLOR_FUENTE + '5. Prestamos')
            print(COLOR_FUENTE + '0. Salir\n') 
            opcion = int(input(COLOR_INPUT + 'Ingrese opción: '))         
            if opcion in range(0,6):
                if opcion   == 0: sys.exit()
                elif opcion == 1: libros.menu_libros()      
                elif opcion == 2: autores.menu_autores()
                elif opcion == 3: categorias.menu_categorias()
                elif opcion == 4: usuarios.menu_usuarios()
                elif opcion == 5: prestamos.menu_prestamos()
            else:
                input(COLOR_ERROR + 'Opción fuera de rango.\n')
        except ValueError:
            input(COLOR_ERROR + 'Opción invalida.\n')

if __name__ == '__main__':
    menu_principal()